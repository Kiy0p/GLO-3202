from django.db import models

from account.models import Account
# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    author = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.title