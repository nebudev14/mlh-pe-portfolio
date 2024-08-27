import datetime
from util.db import mydb
from peewee import *


class TimelinePost(Model):
  name = CharField()
  email = CharField()
  content = TextField()
  created_at = DateTimeField(default=datetime.datetime.now)

  class Meta:
    database = mydb
