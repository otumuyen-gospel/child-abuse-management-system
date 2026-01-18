from .models import Abuse
from .serializers import AbuseSerializers
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
class AbuseList(generics.ListAPIView):
    queryset = Abuse.objects.all()
    serializer_class = AbuseSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='view_abuse')
    name = 'abuse-list'

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    #you can filter by field names specified here keyword e.g url?name='church one'
    filterset_fields = ('type','description',) 

     #you can search using the "search" keyword
    search_fields =  ('type','description',)  

    #you can order using the "ordering" keyword
    ordering_fields =  ('type','description',) 


class UpdateAbuse(generics.UpdateAPIView):
    queryset = Abuse.objects.all()
    serializer_class = AbuseSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='change_abuse')
    name = 'abuse-update'
    lookup_field = "id"

class DeleteAbuse(generics.DestroyAPIView):
    queryset = Abuse.objects.all()
    serializer_class = AbuseSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='delete_abuse')
    name = 'abuse-delete'
    lookup_field = "id"

class CreateAbuse(generics.CreateAPIView):
    queryset = Abuse.objects.all()
    serializer_class = AbuseSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='add_abuse')
    name = 'abuse-create'