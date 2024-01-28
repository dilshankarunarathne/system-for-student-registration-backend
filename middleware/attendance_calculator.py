def get_percentage(attendance_data):
    current_percentage = 0
    for i in attendance_data:
        i['percentage'] = (i['attended_time'] / i['total_time']) * 100
    pass  # TODO
