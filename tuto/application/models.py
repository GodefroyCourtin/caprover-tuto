from django.db import models
from django.contrib.auth.models import AbstractUser


class Myuser(AbstractUser):
    adminn = models.BooleanField(default=False)