from pony.orm import *
from pony.orm.serialization import to_dict

db = Database()
db.bind(provider='mysql', host='192.168.50.7', user='db_user', passwd='some_pass', db='person')


class Person(db.Entity):
    name = PrimaryKey(str)
    surname = Required(str)


class Car(db.Entity):
    name = PrimaryKey(str)
    make = Optional(str)
    year = Optional(str)
