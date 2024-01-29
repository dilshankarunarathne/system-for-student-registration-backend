from dao.class_dao import insert_class_info, query_class_info


def add_new_class(course_id, date, start_time, duration):
    return insert_class_info(course_id, date, start_time, duration)


def get_class_info(course_id):
    return query_class_info(course_id)
