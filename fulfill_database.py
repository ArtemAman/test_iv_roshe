from datetime import date

from peewee import *
import names

# TODO в рамках тестового примера использовал pewee и sqlite. В нормальном примере использовал бы postgres и pony orm

db = SqliteDatabase('people.db')


class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField

    class Meta:
        database = db


Person.create_table()


def make_base_data():
    """
    Для наполнения базы данных
    :return:
    """

    names_list = []
    for _ in range(1111):
        name = names.get_full_name()
        names_list.append(name)
    print(names_list)

    for name in names_list:
        Person.create(name=name, birthday=date(1935, 3, 1), is_relative=True)


if __name__ == '__main__':
    make_base_data()
