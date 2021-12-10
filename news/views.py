from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from .models import  *
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import BasicAuthentication
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated, DjangoModelPermissions]
    filterset_fields = ['name', 'date']
    filter_backends = [filters.OrderingFilter,DjangoFilterBackend,filters.SearchFilter]
    ordering_fields = ['name', '']
    ordering = ['description']
    search_fields = ['name']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class NewsNumberPaginations(PageNumberPagination):
    page_size = 3



# Create your views here.
