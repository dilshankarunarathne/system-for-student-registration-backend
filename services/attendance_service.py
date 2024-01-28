from dao.attendance_dao import query_attendance_info_for_student, query_attendance_info_for_class, delete_all_documents


def get_attendance_info_for_student(student_id):
    return query_attendance_info_for_student(student_id)


def get_attendance_info_for_lecture(course_id, date):
    return query_attendance_info_for_class(course_id, date)


def clear_all_records():
    return delete_all_documents()


def mark_attendance(student_id, course_id, date, attended_time, total_time):
    attendance_info = get_attendance_info_for_lecture(course_id, date)
    if attendance_info is None:
        attendance_info = {
            'course_id': course_id,
            'date': date,
            "student_id": student_id,
            "attended_time": attended_time,
            "total_time": total_time
        }
    else:
        attendance_info['students'] = attendance_info['students'] if 'students' in attendance_info else []
    attendance_info['students'].append({
        'student_id': student_id,
        'attended_time': attended_time
    })
    return attendance_info


