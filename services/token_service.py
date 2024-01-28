from dao.token_dao import blacklist_token, is_token_blacklisted


def add_token_to_blacklist(token: str):
    blacklist_token(token)


def check_if_token_is_blacklisted(token: str) -> bool:
    return is_token_blacklisted(token)
