from datetime import datetime


def parser_date_format(data: str):
    data_obj = datetime.strptime(data, "%Y-%m-%d")
    data_brasileira = data_obj.strftime("%d/%m/%Y")
    return data_brasileira
