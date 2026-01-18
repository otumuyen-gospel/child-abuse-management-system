from .models import Allegation
from .serializers import AllegationSerializer
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
class AllegationList(generics.ListAPIView):
    queryset = Allegation.objects.all()
    serializer_class = AllegationSerializer
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='view_allegation')
    name = 'allegation-list'

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    #you can filter by field names specified here keyword e.g url?name='church one'
    filterset_fields = ('perpetratorId__id','victimId__id','abuse_typeId__id','severity_ranking',
                        'disposition_code',) 

     #you can search using the "search" keyword
    search_fields =  ('perpetratorId__id','victimId__id','abuse_typeId__id','severity_ranking',
                        'disposition_code',)  

    #you can order using the "ordering" keyword
    ordering_fields =  ('perpetratorId__id','victimId__id','abuse_typeId__id','severity_ranking',
                        'disposition_code',) 


class UpdateAllegation(generics.UpdateAPIView):
    queryset = Allegation.objects.all()
    serializer_class = AllegationSerializer
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='change_allegation')
    name = 'allegation-update'
    lookup_field = "id"

class DeleteAllegation(generics.DestroyAPIView):
    queryset = Allegation.objects.all()
    serializer_class = AllegationSerializer
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='delete_allegation')
    name = 'allegation-delete'
    lookup_field = "id"

class CreateAllegation(generics.CreateAPIView):
    queryset = Allegation.objects.all()
    serializer_class = AllegationSerializer
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='add_allegation')
    name = 'allegation-create'