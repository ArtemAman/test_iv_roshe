import datetime
import sqlite3
import pandas as pd
from pandas import ExcelWriter


def make_new_sheet_xlsx(xlsx_file, name_of_new_list):
    """

    :param xlsx_file: файл в который будут добавляться данные
    :param name_of_new_list: название нового листа в файле
    :return:
    """
    con = sqlite3.connect('people.db')
    df = pd.read_sql("SELECT * FROM Person", con)
    try:
        with ExcelWriter(xlsx_file, engine="openpyxl", mode="a") as writer:
            df.to_excel(writer, sheet_name=name_of_new_list)
    except ValueError:
        now = datetime.datetime.now().strftime("%m-%d-%Y, %H-%M-%S")
        with ExcelWriter(xlsx_file, engine="openpyxl", mode="a") as writer:
            df.to_excel(writer, sheet_name=f'{name_of_new_list} {now}')


if __name__ == '__main__':
    make_new_sheet_xlsx('orders.xlsx', 'sheet_2')
