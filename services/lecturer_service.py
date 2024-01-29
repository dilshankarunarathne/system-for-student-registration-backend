from dao.lecturer_dao import query_lecturer_info_by_id


def get_lecturer_by_id(lecturer_id):
    return query_lecturer_info_by_id(lecturer_id)
