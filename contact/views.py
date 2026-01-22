from .models import Contact
from .serializers import ContactSerializers
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
class ContactList(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='view_contact')
    name = 'contact-list'

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    #you can filter by field names specified here keyword e.g url?name='church one'
    filterset_fields = ('personId__id','address','email','phone','socialMedia',
                        'ethnicity','state','occupation', 'country','marital_status') 

     #you can search using the "search" keyword
    search_fields = ('personId__id','address','email','phone','socialMedia',
                        'ethnicity','state','occupation', 'country','marital_status')  

    #you can order using the "ordering" keyword
    ordering_fields = ('personId__id','address','email','phone','socialMedia',
                        'ethnicity','state','occupation', 'country','marital_status')
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


class UpdateContact(generics.UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='change_contact')
    name = 'contact-update'
    lookup_field = "id"
    def get_object(self):
        obj = super().get_object()
        if self.request.user.is_superuser or \
             obj.personId.id == self.request.user.personId.id:
            return obj
        else:
            raise PermissionDenied("You do not have permission to edit this object.")

class DeleteContact(generics.DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='delete_contact')
    name = 'delete-contact'
    lookup_field = "id"
    def get_object(self):
        obj = super().get_object()
        if self.request.user.is_superuser or \
             obj.personId.id == self.request.user.personId.id:
            return obj
        else:
            raise PermissionDenied("You do not have permission to edit this object.")

class CreateContact(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
    permission_classes = [IsAuthenticated, IsInGroup,]
    required_groups = requiredGroups(permission='add_contact')
    name = 'create-contact'