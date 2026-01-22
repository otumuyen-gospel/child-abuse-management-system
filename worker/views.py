from .models import Worker
from .serializers import WorkerSerializers
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
class WorkerList(generics.ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='view_worker')
    name = 'worker-list'

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    #you can filter by field names specified here keyword e.g url?name='church one'
    filterset_fields = ('personId__id','agencyId__id','contactId__id',) 

     #you can search using the "search" keyword
    search_fields =  ('personId__id','agencyId__id','contactId__id',)  

    #you can order using the "ordering" keyword
    ordering_fields =  ('personId__id','agencyId__id','contactId__id',) 


class UpdateWorker(generics.UpdateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='change_worker')
    name = 'worker-update'
    lookup_field = "id"
    def get_object(self):
        obj = super().get_object()
        if self.request.user.is_superuser or \
             obj.personId.id == self.request.user.personId.id:
            return obj
        else:
            raise PermissionDenied("You do not have permission to edit this object.")

class DeleteWorker(generics.DestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='delete_worker')
    name = 'worker-delete'
    lookup_field = "id"
    def get_object(self):
        obj = super().get_object()
        if self.request.user.is_superuser or \
             obj.personId.id == self.request.user.personId.id:
            return obj
        else:
            raise PermissionDenied("You do not have permission to edit this object.")

class CreateWorker(generics.CreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='add_worker')
    name = 'worker-create'