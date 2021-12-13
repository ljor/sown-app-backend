from enum import unique
from peewee import *

from peewee import database_required

DATABASE = SqliteDatabase('seeds.sqlite')

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

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Seed], safe= True)
    print("Connected to the database and created tables if they didn't already exist")
    DATABASE.close()