from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255, unique=True)

class Account(models.Model):
    id = models.AutoField
    account_domain = models.CharField(max_length=100)
    account_username = models.CharField(max_length=50)
    account_password = models.CharField(max_length=10)
    username = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )