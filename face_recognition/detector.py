import pickle
import face_recognition
from pathlib import Path
from collections import Counter
from PIL import Image, ImageDraw

DEFAULT_ENCODINGS_PATH = Path("output/encodings.pkl")

Path("training").mkdir(exist_ok=True)
Path("output").mkdir(exist_ok=True)
Path("validation").mkdir(exist_ok=True)

BOUNDING_BOX_COLOR = "blue"
TEXT_COLOR = "white"

import base64
import numpy as np
import cv2


def recognize_faces_in_base64(
        base64_image: str,
        model: str = "hog",
        encodings_location: Path = DEFAULT_ENCODINGS_PATH,
) -> str:
    # Decode the base64 image
    image_data = base64.b64decode(base64_image)
    nparr = np.frombuffer(image_data, np.uint8)
    input_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert the image from BGR color (which OpenCV uses) to RGB color
    rgb_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

    # Find the face locations and encodings in the image
    input_face_locations = face_recognition.face_locations(rgb_image, model=model)
    input_face_encodings = face_recognition.face_encodings(rgb_image, input_face_locations)

    # Load the known face encodings
    with encodings_location.open(mode="rb") as f:
        loaded_encodings = pickle.load(f)

    # Recognize the faces in the image
    for unknown_encoding in input_face_encodings:
        name = _recognize_face(unknown_encoding, loaded_encodings)
        if not name:
            name = "Unknown"
        return name

    return None


def recognize_faces(
        image_location: str,
        model: str = "hog",
        encodings_location: Path = DEFAULT_ENCODINGS_PATH,
) -> None:
    with encodings_location.open(mode="rb") as f:
        loaded_encodings = pickle.load(f)

    input_image = face_recognition.load_image_file(image_location)

    input_face_locations = face_recognition.face_locations(
        input_image, model=model
    )
    input_face_encodings = face_recognition.face_encodings(
        input_image, input_face_locations
    )

    pillow_image = Image.fromarray(input_image)
    draw = ImageDraw.Draw(pillow_image)

    for bounding_box, unknown_encoding in zip(
            input_face_locations, input_face_encodings
    ):
        name = _recognize_face(unknown_encoding, loaded_encodings)
        if not name:
            name = "Unknown"
        # print(name, bounding_box)
        _display_face(draw, bounding_box, name)

    del draw
    pillow_image.show()


def _recognize_face(unknown_encoding, loaded_encodings):
    boolean_matches = face_recognition.compare_faces(
        loaded_encodings["encodings"], unknown_encoding
    )
    votes = Counter(
        name
        for match, name in zip(boolean_matches, loaded_encodings["names"])
        if match
    )
    if votes:
        return votes.most_common(1)[0][0]


def _display_face(draw, bounding_box, name):
    top, right, bottom, left = bounding_box
    draw.rectangle(((left, top), (right, bottom)), outline=BOUNDING_BOX_COLOR)
    text_left, text_top, text_right, text_bottom = draw.textbbox(
        (left, bottom), name
    )
    draw.rectangle(
        ((text_left, text_top), (text_right, text_bottom)),
        fill="blue",
        outline="blue",
    )
    draw.text(
        (text_left, text_top),
        name,
        fill="white",
    )
