from django.db import models


# Create your models here.

class CompanyName(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=64)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    category = models.OneToOneField(Category, on_delete=models.CASCADE, primary_key=True)
