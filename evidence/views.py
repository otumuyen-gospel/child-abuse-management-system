from urllib import request
from django.shortcuts import render
from .models import Evidence
from .serializers import EvidenceSerializers
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
from django.http import HttpResponse, FileResponse
from rest_framework.views import APIView
from role.util import requiredGroups
from user.permissions import IsInGroup

#this generic class will handle GET method to be used by the admin alone
class EvidenceList(generics.ListAPIView):
    queryset = Evidence.objects.all()
    serializer_class = EvidenceSerializers
    permission_classes = [IsAuthenticated,IsInGroup]
    required_groups = requiredGroups(permission='view_evidence')
    name = 'evidence-list'

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    #you can filter by field names specified here keyword e.g url?name='church one'
    filterset_fields = ('reportId__id',) 

     #you can search using the "search" keyword
    search_fields = ('reportId__id')

    #you can order using the "ordering" keyword
    ordering_fields = ('reportId__id',)


class UpdateEvidence(generics.UpdateAPIView):
    queryset = Evidence.objects.all()
    serializer_class = EvidenceSerializers
    permission_classes = [IsAuthenticated, IsInGroup]
    required_groups = requiredGroups(permission='change_evidence')
    name = 'evidence-update'
    lookup_field = "id"

class DeleteEvidence(generics.DestroyAPIView):
    queryset = Evidence.objects.all()
    serializer_class = EvidenceSerializers
    permission_classes = [IsAuthenticated, IsInGroup]
    required_groups = requiredGroups(permission='delete_evidence')
    name = 'delete-evidence'
    lookup_field = "id"

class CreateEvidence(generics.CreateAPIView):
    queryset = Evidence.objects.all()
    serializer_class = EvidenceSerializers
    permission_classes = [IsAuthenticated, IsInGroup]
    required_groups = requiredGroups(permission='add_evidence')
    name = 'create-evidence'

    