from pprint import pprint

import pandas as pd
import datetime
import dateutil.relativedelta

january = '2020-01-01'
november = '2020-11-01'


def check_good_and_bad(deadline_date, xlsx_file):
    """

    :param deadline_date: принимает на вход дату в виде строки YYYY-mm-dd
    :param xlsx_file: принимает на вход файл с расширением xlsx
    :return: возвращает длину списка  хороших и плохих покупателей
    """
    table = pd.read_excel(xlsx_file)
    good_boys = []
    bad_boys = []
    deadline_date_datetime = datetime.datetime.strptime(deadline_date, '%Y-%m-%d')
    six_month_earlier_datetime = deadline_date_datetime - dateutil.relativedelta.relativedelta(months=6)
    for row in table.values:
        if deadline_date_datetime > row[1] >= six_month_earlier_datetime:
            good_boys.append(row[0])
        elif row[1] < six_month_earlier_datetime:
            bad_boys.append(row[0])
        else:
            pass
            # print(f'Этот парнишка {row[0]}покупал позже 1 числа контрольного меясца')

    return len(good_boys), len(bad_boys)


if __name__ == '__main__':
    jan = check_good_and_bad(january, 'orders.xlsx')
    print(f'Хорошие покупатели по состоянию на явнварь {jan[0]} человек')
    nov = check_good_and_bad(november, 'orders.xlsx')
    print(f'Хорошие покупатели по состоянию на ноябрь {nov[0]} человек, плохие {nov[1]} человек')
