from django.contrib import admin
from .models import User, student, teacher, Admin
# Register your models here.
admin.site.register(User)
admin.site.register(student)
admin.site.register(teacher)
admin.site.register(Admin)


