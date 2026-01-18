from .models import Report, Report
from .serializers import ReportSerializers
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
class ReportList(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='view_report')
    name = 'report-list'

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    #you can filter by field names specified here keyword e.g url?name='church one'
    filterset_fields = ('reporterId__id','source','summary','status',) 

     #you can search using the "search" keyword
    search_fields =  ('reporterId__id','source','summary','status',)  

    #you can order using the "ordering" keyword
    ordering_fields =  ('reporterId__id','source','summary','status',) 


class UpdateReport(generics.UpdateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='change_report')
    name = 'report-update'
    lookup_field = "id"

class DeleteReport(generics.DestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='delete_report')
    name = 'report-delete'
    lookup_field = "id"

class CreateReport(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='add_report')
    name = 'report-create'