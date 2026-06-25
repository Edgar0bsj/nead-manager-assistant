from unidecode import unidecode
from fuzzywuzzy import fuzz
from src.apps.cursos.util.mapper_cursos import (
    MAPPER_CURSOS_EXTERNOID,
    MAPPER_COURSE_TYPE_ID,
)


def normalize_text(element):
    strFormat = str(element).strip().lower()
    strFormat = unidecode(strFormat)
    strFormat = " ".join(strFormat.split())
    # strFormat = strFormat.replace("-", "")
    return strFormat


def is_equals(s1: str, s2: str):

    ratio = fuzz.ratio(s1, s2)
    partial = fuzz.partial_ratio(s1, s2)

    # score = (ratio + partial) / 2

    score = (ratio * 0.4) + (partial * 0.6)
    return score


def set_externalId(element, func_normalize=normalize_text, isEquals=is_equals):

    _externalId: str | None = None
    score = 0

    curso = func_normalize(str(element)).replace("-", "")

    for key, value in MAPPER_CURSOS_EXTERNOID.items():
        score_new = isEquals(key, curso)

        if (score_new >= 90) and (score_new >= score):
            score = score_new
            _externalId = value

    return _externalId


def set_courseTypeId(externalId, func_normalize=normalize_text, isEquals=is_equals):
    externalId = func_normalize(str(externalId))
    score = 0
    _courseTypeId: str | None = None

    for external_id, typeId in MAPPER_COURSE_TYPE_ID.items():
        score_new = isEquals(externalId, func_normalize(external_id))

        if (score_new >= 90) and (score_new >= score):
            score = score_new
            _courseTypeId = typeId

    return _courseTypeId
