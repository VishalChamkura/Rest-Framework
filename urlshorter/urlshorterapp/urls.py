from django.urls import path
from .views import *

urlpatterns = [
    path("api/create",Createshorturl),
    path("<str:shorturl>",RedirectToLongurl)
]
