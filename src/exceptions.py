class BaseError(Exception):
    pass


class InvalidCredentials(BaseError):
    pass


class UserIsBlocked(BaseError):
    pass
