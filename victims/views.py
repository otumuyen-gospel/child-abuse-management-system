from .models import Victim
from .serializers import VictimSerializers
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
class VictimList(generics.ListAPIView):
    queryset = Victim.objects.all()
    serializer_class = VictimSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='view_victim')
    name = 'victim-list'

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    #you can filter by field names specified here keyword e.g url?name='church one'
    filterset_fields = ('contactId__id','personId__id',) 

     #you can search using the "search" keyword
    search_fields =  ('contactId__id','personId__id',)  

    #you can order using the "ordering" keyword
    ordering_fields =  ('contactId__id','personId__id',) 


class UpdateVictim(generics.UpdateAPIView):
    queryset = Victim.objects.all()
    serializer_class = VictimSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='change_victim')
    name = 'victim-update'
    lookup_field = "id"

class DeleteVictim(generics.DestroyAPIView):
    queryset = Victim.objects.all()
    serializer_class = VictimSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='delete_victim')
    name = 'victim-delete'
    lookup_field = "id"

class CreateVictim(generics.CreateAPIView):
    queryset = Victim.objects.all()
    serializer_class = VictimSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='add_victim')
    name = 'victim-create'