from django.contrib import admin
from.models import BookModel


class BookModelAdmin(admin.ModelAdmin):
    list_display = ["name","author","price",]


# Register your models here.
admin.site.register(BookModel,BookModelAdmin)