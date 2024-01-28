from bson import json_util
from dao.attendance_dao import query_attendance_info_for_student, query_attendance_info_for_class, delete_all_documents, \
    query_mark_attendance, insert_placeholder_document


def get_attendance_info_for_student(student_id):
    data = query_attendance_info_for_student(student_id)
    data['_id'] = str(data['_id'])
    return data


def get_attendance_info_for_lecture(course_id, date):
    return query_attendance_info_for_class(course_id, date)


def create_placeholder_document():
    insert_placeholder_document()


def clear_all_records():
    return delete_all_documents()


def mark_attendance(student_id, course_id, date, attended_time, total_time):
    attendance_info = {
        "student_id": student_id,
        "course_id": course_id,
        "date": date,
        "attended_time": attended_time,
        "total_time": total_time
    }
    return query_mark_attendance(attendance_info)
