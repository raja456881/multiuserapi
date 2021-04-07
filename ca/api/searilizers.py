from .models import User, student, teacher, Admin
from rest_framework import serializers
from rest_framework import status
from django.db import transaction


class studentsearilizers(serializers.ModelSerializer):

	class Meta:
		model=User
		fields=('email', 'username', 'password')

	def create(self, validated_data):
		username = validated_data['username']
		email = validated_data['email']
		user=User.objects.create_user(**validated_data, is_student=True, is_teacher=False, is_admin=False)
		stu1=student.objects.create(user=user, username=username, email=email)

		return user


class teachersearilizers(serializers.ModelSerializer):

	class Meta:
		model=User
		fields=('email', 'username', 'password' )

	def create(self, validated_data):
		username = validated_data['username']
		email = validated_data['email']
		user=User.objects.create_user(**validated_data, is_student=False, is_teacher=True, is_admin=False)
		stu1=teacher.objects.create(user=user, username=username, email=email)
		return user

class adminsearilizers(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=('email', 'username', 'password' )

	def create(self, validated_data):
		username=validated_data['username']
		email=validated_data['email']
		user=User.objects.create_user(**validated_data, is_student=False, is_teacher=False, is_admin=True, is_superuser=True, is_staff=True)
		stu1=Admin.objects.create(user=user, username=username, email=email )
		return user


class userseariizers(serializers.ModelSerializer):
	class Meta:
		model=User
		fields = ('email', 'username', 'password', 'is_student', 'is_teacher', 'is_admin')


class studentlistsearilizers(serializers.ModelSerializer):
	class Meta:
		model=student
		fields=('email', 'username')


