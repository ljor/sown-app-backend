from enum import unique
from peewee import *
import os

from flask_login import UserMixin
from peewee import database_required

from playhouse.db_url import connect

DATABASE = connect(os.environ.get('DATABASE_URL') or 'sqlite:///dogs.sqlite')

class User(UserMixin, Model):
    username = CharField()
    email = CharField(unique=True)
    password = CharField()
    zip = IntegerField()

    class Meta:
        database = DATABASE

class Seed(Model): 
    name = CharField()
    category = CharField()
    indoor_sow_start = IntegerField()
    indoor_sow_end = IntegerField()
    direct_sow_start = IntegerField()
    direct_sow_end = IntegerField()
    img = CharField()
    maturity = CharField()
    description = TextField()

    class Meta:
        database = DATABASE

class UserSeed(Model):
    user = ForeignKeyField(User)
    seed = ForeignKeyField(Seed)

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Seed, UserSeed], safe= True)
    print("Connected to the database and created tables if they didn't already exist")
    DATABASE.close()