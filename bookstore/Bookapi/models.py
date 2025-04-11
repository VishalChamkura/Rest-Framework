from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BookModel(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None,null=True)
    # author = models.CharField(max_length=100)

    price = models.IntegerField()