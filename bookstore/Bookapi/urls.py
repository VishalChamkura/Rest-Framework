from django.urls import path,include
from .api import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('router',BookViewSet)

urlpatterns = [
    # path("list",BookListApi),
    # path("create",BookCreateApi),
    # path("update/<int:id>",BookUpdateApi),
    # path("delete/<int:id>",BookDeleteApi)
    path("",include(router.urls))
]
