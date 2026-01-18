from .models import Agency
from .serializers import AgencySerializers
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
class AgencyList(generics.ListAPIView):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='view_agency')
    name = 'agency-list'

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    #you can filter by field names specified here keyword e.g url?name='church one'
    filterset_fields = ('name','address','description',) 

     #you can search using the "search" keyword
    search_fields = ('name','address','description',) 

    #you can order using the "ordering" keyword
    ordering_fields = ('name','address','description',) 


class UpdateAgency(generics.UpdateAPIView):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='change_agency')
    name = 'agency-update'
    lookup_field = "id"

class DeleteAgency(generics.DestroyAPIView):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='delete_agency')
    name = 'agency-delete'
    lookup_field = "id"

class CreateAgency(generics.CreateAPIView):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='add_agency')
    name = 'create-agency'