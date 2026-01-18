from .models import Investigation
from .serializers import InvestigationSerializer
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
class InvestigationList(generics.ListAPIView):
    queryset = Investigation.objects.all()
    serializer_class = InvestigationSerializer
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='view_investigation')
    name = 'investigation-list'

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    #you can filter by field names specified here keyword e.g url?name='church one'
    filterset_fields = ('allegationId__id','safety_plan_status','response_type',) 

     #you can search using the "search" keyword
    search_fields =  ('allegationId__id','safety_plan_status','response_type',)  

    #you can order using the "ordering" keyword
    ordering_fields =  ('allegationId__id','safety_plan_status','response_type',) 


class UpdateInvestigation(generics.UpdateAPIView):
    queryset = Investigation.objects.all()
    serializer_class = InvestigationSerializer
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='change_investigation')
    name = 'investigation-update'
    lookup_field = "id"

class DeleteInvestigation(generics.DestroyAPIView):
    queryset = Investigation.objects.all()
    serializer_class = InvestigationSerializer
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='delete_investigation')
    name = 'investigation-delete'
    lookup_field = "id"

class CreateInvestigation(generics.CreateAPIView):
    queryset = Investigation.objects.all()
    serializer_class = InvestigationSerializer
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='add_investigation')
    name = 'investigation-create'