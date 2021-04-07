from django.urls import path,include
from.import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

rounter=DefaultRouter()

rounter.register("student/register",views.studentresgister, basename="stundentregister")
rounter.register("teacher/register", views.teacheresgister, basename="teacherregister")
rounter.register("admin/register", views.adminesgister, basename="adminregister")
rounter.register("teacher/list", views.teacherlist, basename='teachlist')
rounter.register("student/list", views.studentlist, basename="studentlist")
rounter.register("user/list", views.UserList,basename="userlist")

urlpatterns = [
	path("", include(rounter.urls)),
	path("gettoken/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
	path("refresh/", TokenRefreshView.as_view(), name="token_refersh"),
	path("verifytoken", TokenVerifyView.as_view(), name="token_verify")
]
