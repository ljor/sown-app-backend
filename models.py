import os
from peewee import *

from flask_login import UserMixin
from peewee import database_required

from playhouse.db_url import connect

# DATABASE = connect(os.environ.get('DATABASE_URL') or 'sqlite://seeds.sqlite')

if 'ON_HEROKU' in os.environ:
    DATABASE = connect(os.environ.get('DATABASE_URL'))

else:
    DATABASE = SqliteDatabase('seeds.sqlite')

class BaseModel(Model):
    class Meta:
        database = DATABASE

class User(UserMixin, BaseModel):
    username = CharField()
    email = CharField(unique=True)
    password = CharField()
    zip = IntegerField()

class Seed(BaseModel): 
    name = CharField()
    category = CharField()
    indoor_sow_start = IntegerField()
    indoor_sow_end = IntegerField()
    direct_sow_start = IntegerField()
    direct_sow_end = IntegerField()
    img = CharField()
    maturity = CharField()
    description = TextField()


class UserSeed(BaseModel):
    user = ForeignKeyField(User)
    seed = ForeignKeyField(Seed)

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Seed, UserSeed], safe=True)
    print("Connected to the database and created tables if they didn't already exist")
    DATABASE.close()