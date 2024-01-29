from dao.class_dao import insert_class_info


def add_new_class(course_id, date, start_time, duration):
    insert_class_info(course_id, date, start_time, duration)
