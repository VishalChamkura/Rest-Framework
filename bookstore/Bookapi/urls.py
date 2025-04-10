from django.urls import path
from .api import *

urlpatterns = [
    path("list",BookListApi),
    path("create",BookCreateApi),
    path("update/<int:id>",BookUpdateApi),
    path("delete/<int:id>",BookDeleteApi)
]
