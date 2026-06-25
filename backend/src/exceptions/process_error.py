class BaseError(Exception):
    def __init__(self, msg: str):
        self.msg = msg


class UniqueConstraintViolationException(BaseError):
    def __init__(self, msg: str):
        super().__init__(msg)


class EntityNotFoundException(BaseError):
    def __init__(self, msg: str):
        super().__init__(msg)
