from.searilizers import studentsearilizers, teachersearilizers, adminsearilizers, userseariizers,\
	studentlistsearilizers
from rest_framework.response import Response
from  rest_framework import status
from rest_framework import viewsets
from .models import User, student
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import  SessionAuthentication, BaseAuthentication
from .permission import adminpermission, teacherpermission, studentpermission
from rest_framework.views import APIView
import http.client
import random
from django.conf import settings


class studentresgister(viewsets.ViewSet):

    def create(self, request):
        searilizers=studentsearilizers(data=request.data)
        if searilizers.is_valid(raise_exception=True):
            searilizers.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(searilizers.errors, status=status.HTTP_400_BAD_REQUEST)


class teacheresgister(viewsets.ViewSet):


    def create(self, request):
        searilizers=teachersearilizers(data=request.data)
        if searilizers.is_valid(raise_exception=True):
            searilizers.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(searilizers.errors, status=status.HTTP_400_BAD_REQUEST)



class adminesgister(viewsets.ViewSet):

    def create(self, request):
        searilizers=adminsearilizers(data=request.data)
        if searilizers.is_valid(raise_exception=True):
            searilizers.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(searilizers.errors, status=status.HTTP_400_BAD_REQUEST)



class UserList(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def list(self, request):
        queryset=User.objects.all()
        serializer_class = userseariizers(queryset, many=True)
        return  Response(serializer_class.data, status=status.HTTP_200_OK)

    def create(self, request):
        searilizers=userseariizers(data=request.data)
        if searilizers.is_valid():
           searilizers.save()
           return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_401_UNAUTHORIZED)




class teacherlist(viewsets.ViewSet):

    def list(self, request):
        queryset = student.objects.all()
        serializer = studentlistsearilizers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self , request):
        searilizers=studentsearilizers(data=request.data)
        if searilizers.is_valid():
           searilizers.save()
           return Response(searilizers.data, status=status.HTTP_201_CREATED)
        return  Response(searilizers.errors, status=status.HTTP_400_BAD_REQUEST)




class studentlist(viewsets.ViewSet):

	def list(self, request):
		user=request.user
		try:
			snippte=student.objects.all().get(user=user)
			serializer = studentlistsearilizers(snippte)
			return Response(serializer.data)

		except:
			return Response({"error": 'user is not exit'}, status=status.HTTP_401_UNAUTHORIZED)











