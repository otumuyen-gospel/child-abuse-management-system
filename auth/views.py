from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers.otp import (PasswordResetRequestSerializer, 
                              OTPVerificationSerializer, 
                              PasswordResetSerializer)
from .serializers.logentry import LogEntrySerializer
from .serializers.register import SignupSerializer
from rest_framework import generics
from auditlog.models import LogEntry
from rest_framework.permissions import IsAuthenticated, IsAdminUser,AllowAny
from user.permissions import IsInGroup
from django.contrib.auth.models import Group
from role.models import Role
from message import EmailService
from agency.models import Agency
from person.models import Person


'''
after blacklisting a token or loging out remember to delete
any storage of tokens details in frontend or browser local
storage to avoid using it again 
'''
class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class PasswordResetRequestAPIView(APIView):
    permission_classes = [AllowAny,]
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            return Response(
                {"success": True, "message": "OTP sent to email."}, 
                status=status.HTTP_200_OK
            )
        return Response(
            {"success": False, "errors": serializer.errors}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    

class OTPVerificationAPIView(APIView):
    permission_classes = [AllowAny,]
    def post(self, request):
        serializer = OTPVerificationSerializer(data=request.data)
        if serializer.is_valid():
            return Response(
                {"success": True, "message": "OTP verified successfully."},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"success": False, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

class PasswordResetAPIView(APIView):
    permission_classes = [AllowAny,]
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": True, "message": "Password reset successfully."},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"success": False, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
class LogEntryViews(generics.ListAPIView):
    queryset = LogEntry.objects.all().order_by('-timestamp')
    serializer_class = LogEntrySerializer
    permission_classes = [IsAuthenticated, IsInGroup]
    #required_groups = ['admin',]
    name = 'user-logs'


class ReporterSignupView(generics.CreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = SignupSerializer
    name='reporter-signup'
    def create(self, request, *args, **kwargs):
        role = Role.objects.get(name='reporter')
        if not role:
            return Response(
                {'error':'No reporter role found, contact admin'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if (not request.data.get('firstName') and not request.data.get('lastName')) and \
            (not request.data.get('middleName') and not request.data.get('maidenName')) and \
                (not request.data.get('dob') and not request.data.get('phone')) and \
            (not request.data.get('email') and not request.data.get('entranceDate')) and \
            not request.data.get('gender'):
            return Response(
                {'error':'username, password, firstName, lastName, middleName, maidenName, dob, phone, email, entranceDate, gender are required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        person = Person.objects.create(
            firstName=request.data.get('firstName'),
            lastName=request.data.get('lastName'),
            middleName=request.data.get('middleName'),
            maidenName=request.data.get('maidenName'),
            dob=request.data.get('dob'),
            phone =request.data.get('phone'),
            email = request.data.get('email'),
            entranceDate=request.data.get('entranceDate'),
            gender = request.data.get('gender'),

        )
        data = request.data.copy()
        data['personId'] = person.id
        data['roleId'] = role.id
        request._full_data = data
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        '''check if user is added to a group otherwise 
        fetch user choosen group and add user to the group
        '''
        group = Group.objects.get(name=role.name)
        user.groups.add(group)

        '''token based authentication instead of 
        direct session, cookie access management
        '''
        refresh = RefreshToken.for_user(user) 
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            }
        
        
        # In your user registration view
        EmailService.send_welcome_email(
         user_email=request.data['email'],
         user_name=request.data['username'],
         agency_name=Agency.objects.first().name,
         roles = role.permissions.split(',')
        )
        
        return Response({"user": serializer.data,
                         "refresh": res["refresh"],
                         "token": res["access"]
                         }, status=status.HTTP_201_CREATED)