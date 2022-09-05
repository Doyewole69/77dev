from audioop import maxpp
from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
from decimal import Decimal
from .managers import UserManager
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    objects = CustomUserManager()

class AccountType(models.Model):
    name = models.CharField(max_length=128)

class ForexDenModel(models.Model):
    Balance = models.CharField(max_length=10)
    Earning = models.CharField(max_length=10)
    Last_Deposit = models.CharField(max_length=10)
    Pending_Withdrawal = models.CharField(max_length=10)
    Referals = models.CharField(max_length=3)
    Earned_Commission = models.CharField(max_length=10)

