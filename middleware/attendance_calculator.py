def get_percentage(attendance_data):
    current_percentage = []
    for i in attendance_data:
        current_percentage.append(i['attended_time'] / i['total_time'])
    for i in current_percentage:
        final_percentage = sum(current_percentage) / len(current_percentage)

    return final_percentage
