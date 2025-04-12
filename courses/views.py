from django.shortcuts import render
from .serializers import CourseSerializer
from .models import CourseModel
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

class CourseView(viewsets.ModelViewSet):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer

