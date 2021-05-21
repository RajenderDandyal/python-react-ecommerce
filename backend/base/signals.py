from django.db.models.signals import pre_save
from django.contrib.auth.models import User


def updateUser(sender, instance, **kwargs):
    print('Signal Trigred')
    user = isinstance
    if user.email != "":
        user.username = user.email
