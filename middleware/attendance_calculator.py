def get_percentage(attendance_data):
    if isinstance(attendance_data, dict):
        attendance_data = [attendance_data]
    elif not all(isinstance(i, dict) for i in attendance_data):
        print(attendance_data)
        print(type(attendance_data))
        raise ValueError("attendance_data must be a list of dictionaries")

    current_percentage = []
    for i in attendance_data:
        a_time = int(i['attended_time'])
        t_time = int(i['total_time'])
        current_percentage.append(a_time / t_time)

    final_percentage = sum(current_percentage) / len(current_percentage)
    if final_percentage < 0.80:
        ext = 0.80 - final_percentage
        ext_type = "shortage"
    elif final_percentage > 0.80:
        ext = final_percentage - 0.80
        ext_type = "excess"

    return final_percentage, ext, ext_type
