from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Custom user model classes
    mobile = models.CharField(max_length=11, unique=True, verbose_name='mobile')

    class Meta:
        db_table = 'tb_user'
        verbose_name = 'user'
        verbose_name_plural = verbose_name

