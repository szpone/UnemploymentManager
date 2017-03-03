from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# a model describing company what we applied to
class Company(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=64)
    company_website = models.CharField(max_length=128)
    offer_website = models.CharField(max_length=128)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    category = models.OneToOneField(Category, on_delete=models.CASCADE, primary_key=True)
    sent_date = models.DateTimeField(auto_now=True)
    comment = models.TextField(blank=True)
    user = models.ForeignKey(User, null=True)


class Position(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)


class Category(models.Model):
    name = models.CharField(max_length=128)
