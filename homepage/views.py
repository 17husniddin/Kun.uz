from django.shortcuts import render
from .serializers import HomepageSerializer
from rest_framework import viewsets
from .models import  *
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import BasicAuthentication
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

class HomepageViewSet(viewsets.ModelViewSet):
    queryset = Homepage.objects.all()
    serializer_class = HomepageSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated, DjangoModelPermissions]
    filterset_fields = ['name', 'price']
    filter_backends = [filters.OrderingFilter,DjangoFilterBackend,filters.SearchFilter]
    ordering_fields = ['name', 'price']
    ordering = ['price']
    search_fields = ['name']


class HomePageNumberPaginations(PageNumberPagination):
    page_size = 3



# Create your views here.
