from enum import Enum

BASE_URL = "http://127.0.0.1:8000"


class TemplatesPages(Enum):
    POLO = "polos/MainPage.html"
    NIVEL_ENSINO = "nivel_ensino/MainPage.html"
    MODALIDADE_ENSINO = "modalidades_ensino/MainPage.html"
    CURSOS = "cursos/MainPage.html"


class APIEndpoints(Enum):
    POLO = "http://127.0.0.1:8080/polo/"
    NIVEL_ENSINO = "http://127.0.0.1:8080/nivel-ensino/"
    MODALIDADE_ENSINO = "http://127.0.0.1:8080/mods-ensino/"
    CURSOS = "http://127.0.0.1:8080/cursos/"
