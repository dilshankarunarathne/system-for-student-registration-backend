import cv2


def save_image(frame, class_name, count):
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imwrite(f"training/{class_name}/{class_name}_{count}.jpg", frame)
    print(f"Image {class_name}_{count} saved successfully")


def store_image_model_info(class_name, student_id):
    with open("training_info.txt", "a") as f:
        f.write(f"{class_name} {student_id}\n")
    print(f"Student {class_name} {student_id} info saved successfully")


def get_student_info():
    student_info = {}
    with open("training_info.txt", "r") as f:
        for line in f:
            class_name, student_id = line.split()
            student_info[class_name] = student_id
    return student_info
