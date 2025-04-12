from typing import Any, Iterable
from django.db import models
from hashids import Hashids

# def generaterandomstring(min_length):
#     import random
#     import string

#     charaters  = string.ascii_letters + string.digits
#     return "".join(random.choice(charaters) for i in range(min_length))


def generaterandomstringbyid(id):
    return Hashids(salt='urlshorterapp',min_length=5).encode(id)

class Urlmodel(models.Model):
    longurl = models.URLField()
    shorturl = models.CharField(max_length=10)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

        self.shorturl = generaterandomstringbyid(self.id)
        super().save(*args,**kwargs)
