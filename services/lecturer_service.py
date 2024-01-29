from dao.lecturer_dao import query_lecturer_info_by_uid


def get_lecturer_by_id(lecturer_id):
    data = query_lecturer_info_by_uid(lecturer_id)