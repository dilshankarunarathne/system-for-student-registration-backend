from dao.course_dao import query_all_courses, query_course_by_id


def get_all_courses():
    return query_all_courses()


def get_course_by_id(_id):
    return query_course_by_id(_id)
