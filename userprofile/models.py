from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Profile(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    descrpition = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.owner.username