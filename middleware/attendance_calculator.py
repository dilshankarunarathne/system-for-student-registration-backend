def get_percentage(attendance_data):
    for i in attendance_data:
        i['percentage'] = (i['attended_time'] / i['total_time']) * 100
    pass  # TODO
