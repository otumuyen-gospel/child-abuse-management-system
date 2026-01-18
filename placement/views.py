from .models import Placement
from .serializers import PlacementSerializer
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
class PlacementList(generics.ListAPIView):
    queryset = Placement.objects.all()
    serializer_class = PlacementSerializer
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='view_placement')
    name = 'placement-list'

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    #you can filter by field names specified here keyword e.g url?name='church one'
    filterset_fields = ('resources','victimId__id','provider','license',
                        'capacity','start_date','end_date') 

     #you can search using the "search" keyword
    search_fields =  ('resources','victimId__id','provider','license',
                        'capacity','start_date','end_date')  
    #you can order using the "ordering" keyword
    ordering_fields =  ('resources','victimId__id','provider','license',
                        'capacity','start_date','end_date') 


class UpdatePlacement(generics.UpdateAPIView):
    queryset = Placement.objects.all()
    serializer_class = PlacementSerializer
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='change_placement')
    name = 'placement-update'
    lookup_field = "id"

class DeletePlacement(generics.DestroyAPIView):
    queryset = Placement.objects.all()
    serializer_class = PlacementSerializer
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='delete_placement')
    name = 'placement-delete'
    lookup_field = "id"

class CreatePlacement(generics.CreateAPIView):
    queryset = Placement.objects.all()
    serializer_class = PlacementSerializer
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='add_placement')
    name = 'placement-create'