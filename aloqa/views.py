from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework import viewsets


# Create your views here.

class CarPageNumberPaginations(PageNumberPagination):
    page_size = 3


class AloqaViewSet(viewsets.ModelViewSet):
    queryset = Aloqa.objects.all()
    serializer_class = AloqaSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend, filters.SearchFilter]
    ordering_fields = ['name', 'subject']
    ordering = ['subject']
    search_fields = ['^name', 'subject']
    filterset_fields = ['name', 'subject']