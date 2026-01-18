from .models import Perpetrator
from .serializers import PerpetratorSerializers
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
class PerpetratorList(generics.ListAPIView):
    queryset = Perpetrator.objects.all()
    serializer_class = PerpetratorSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='view_perpetrator')
    name = 'perpetrator-list'

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    #you can filter by field names specified here keyword e.g url?name='church one'
    filterset_fields = ('contactId__id','personId__id',) 

     #you can search using the "search" keyword
    search_fields =  ('contactId__id','personId__id',)  

    #you can order using the "ordering" keyword
    ordering_fields =  ('contactId__id','personId__id',) 


class UpdatePerpetrator(generics.UpdateAPIView):
    queryset = Perpetrator.objects.all()
    serializer_class = PerpetratorSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='change_perpetrator')
    name = 'perpetrator-update'
    lookup_field = "id"

class DeletePerpetrator(generics.DestroyAPIView):
    queryset = Perpetrator.objects.all()
    serializer_class = PerpetratorSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='delete_perpetrator')
    name = 'perpetrator-delete'
    lookup_field = "id"

class CreatePerpetrator(generics.CreateAPIView):
    queryset = Perpetrator.objects.all()
    serializer_class = PerpetratorSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='add_perpetrator')
    name = 'perpetrator-create'