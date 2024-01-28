def get_attendance_info_for_student(student_id):
    filt = {'student_id': student_id}
    attendance = user_collection.find_one(filt)
    return attendance