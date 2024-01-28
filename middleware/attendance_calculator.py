def get_percentage(attendance_data):
    current_percentage = []
    for i in attendance_data:
        a_time = int(i['attended_time'])
        current_percentage.append(a_time / i['total_time'])

    final_percentage = sum(current_percentage) / len(current_percentage)
    if final_percentage < 0.80:
        ext = 0.80 - final_percentage
        ext_type = "shortage"
    elif final_percentage > 0.80:
        ext = final_percentage - 0.80
        ext_type = "excess"

    return final_percentage, ext, ext_type
