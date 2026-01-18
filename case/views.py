from .models import Case
from .serializers import CaseSerializers
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
class CaseList(generics.ListAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='view_case')
    name = 'case-list'

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    #you can filter by field names specified here keyword e.g url?name='church one'
    filterset_fields = ('reporterId__id','reportId__id','workerId__id','perpetratorId__id',
                        'victimId__id','abusseTypeId__id','startDate','endDate',
                        'outcome',) 

     #you can search using the "search" keyword
    search_fields =  ('reporterId__id','reportId__id','workerId__id','perpetratorId__id', 
                      'victimId__id','abusseTypeId__id','startDate','endDate',
                        'outcome',)  

    #you can order using the "ordering" keyword
    ordering_fields =  ('reporterId__id','reportId__id','workerId__id','perpetratorId__id',
                        'victimId__id','abusseTypeId__id','startDate','endDate',
                        'outcome',)  

class UpdateCase(generics.UpdateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='change_case')
    name = 'case-update'
    lookup_field = "id"

class DeleteCase(generics.DestroyAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='delete_case')
    name = 'case-delete'
    lookup_field = "id"

class CreateCase(generics.CreateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='add_case')
    name = 'case-create'