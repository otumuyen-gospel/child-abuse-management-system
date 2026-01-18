from .models import Service
from .serializers import ServiceSerializers
from django.shortcuts import render
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from urllib.parse import urlparse
from rest_framework.permissions import IsAuthenticated, IsAdminUser,AllowAny
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter
from rest_framework.exceptions import PermissionDenied
from django.http import HttpResponse
from role.util import requiredGroups
from user.permissions import IsInGroup



#this generic class will handle GET method to be used by the admin alone
class ServiceList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='view_service')
    name = 'service-list'

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    #you can filter by field names specified here keyword e.g url?name='church one'
    filterset_fields = ('type','description','date','victimId__id') 

     #you can search using the "search" keyword
    search_fields =  ('type','description', 'date','victimId__id')  

    #you can order using the "ordering" keyword
    ordering_fields =  ('type','description', 'date','victimId__id') 


class UpdateService(generics.UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='change_abuse')
    name = 'abuse-update'
    lookup_field = "id"

class DeleteAService(generics.DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='delete_abuse')
    name = 'abuse-delete'
    lookup_field = "id"

class CreateService(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='add_service')
    name = 'service-create'