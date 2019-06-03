from pony.orm import *
from pony.orm.serialization import to_dict

db = Database()
db.bind(provider='mysql', host='192.168.50.7', user='usermanager_db_user', passwd='password_1', db='usermanager')

class Person(db.Entity):
    id = PrimaryKey(str)
    name = Required(str)
    lastname = Required(str)

db.generate_mapping(create_tables=True)

if __name__ == '__main__':    

    with db_session:
        Person(id='asf7',
               name='Jill',
               lastname='Doe')
