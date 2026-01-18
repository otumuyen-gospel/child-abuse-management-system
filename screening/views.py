from .models import Screening
from .serializers import ScreeningSerializers
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
class ScreeningList(generics.ListAPIView):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='view_screening')
    name = 'screening-list'

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    #you can filter by field names specified here keyword e.g url?name='church one'
    filterset_fields = ('outcome','review_team_approval','reportId__id') 

     #you can search using the "search" keyword
    search_fields =  ('outcome','review_team_approval', 'reportId__id')  

    #you can order using the "ordering" keyword
    ordering_fields =  ('outcome','review_team_approval', 'reportId__id') 


class UpdateScreening(generics.UpdateAPIView):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='change_screening')
    name = 'screening-update'
    lookup_field = "id"

class DeleteAScreening(generics.DestroyAPIView):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='delete_screening')
    name = 'screening-delete'
    lookup_field = "id"

class CreateScreening(generics.CreateAPIView):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='add_screening')
    name = 'screening-create'