def save_image(frame, class_name, count):
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imwrite(f"training/{class_name}/{class_name}_{count}.jpg", frame)
    print("Image saved successfully")