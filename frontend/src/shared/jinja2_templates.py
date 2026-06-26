from fastapi.templating import Jinja2Templates


def templating(_directory: str = "src/view/html"):
    TEMPLATING = Jinja2Templates(directory=_directory)

    return TEMPLATING
