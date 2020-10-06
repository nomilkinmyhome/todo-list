class BaseError(Exception):
    pass


class InvalidEmail(BaseError):
    pass


class InvalidCredentials(BaseError):
    pass


class UserIsBlocked(BaseError):
    pass
