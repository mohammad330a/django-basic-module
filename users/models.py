from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created at'
    )

    def __str__(self):
        return str(self.pk) + " ) " + self.username + ' : ' + self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
