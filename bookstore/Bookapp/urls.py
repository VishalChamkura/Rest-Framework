from django.urls import path
from .api import *

urlpatterns = [
    path("create",Usercreateapi),
    # path("login",Userloginapi),
    path("protect",protectedView)
]