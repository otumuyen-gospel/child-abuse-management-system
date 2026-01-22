from .models import Reporter
from .serializers import ReporterSerializers
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
class ReporterList(generics.ListAPIView):
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='view_reporter')
    name = 'reporter-list'

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    #you can filter by field names specified here keyword e.g url?name='church one'
    filterset_fields = ('contactId__id','personId__id',) 

     #you can search using the "search" keyword
    search_fields =  ('contactId__id','personId__id',)  

    #you can order using the "ordering" keyword
    ordering_fields =  ('contactId__id','personId__id',) 
    def get_queryset(self):
        person = self.request.user.personId
        if self.request.user.is_superuser:
            return self.queryset
        elif self.request.user.roleId.name == 'case_worker':
            return self.queryset
        elif person is not None:
            return self.queryset.filter(personId=person.id)
        else:
            raise PermissionDenied("You don't have access right")


class UpdateReporter(generics.UpdateAPIView):
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='change_reporter')
    name = 'reporter-update'
    lookup_field = "id"
    def get_object(self):
        obj = super().get_object()
        if self.request.user.is_superuser or \
             obj.personId.id == self.request.user.personId.id:
            return obj
        else:
            raise PermissionDenied("You do not have permission to edit this object.")

class DeleteReporter(generics.DestroyAPIView):
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='delete_reporter')
    name = 'reporter-delete'
    lookup_field = "id"
    def get_object(self):
        obj = super().get_object()
        if self.request.user.is_superuser or \
             obj.personId.id == self.request.user.personId.id:
            return obj
        else:
            raise PermissionDenied("You do not have permission to edit this object.")

class CreateReporter(generics.CreateAPIView):
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='add_reporter')
    name = 'reporter-create'