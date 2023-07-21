from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard', views.UserDashBoard, name="dashboard"),
    path('signIn', views.signIn, name="login"),
    path('signUp', views.signUp, name="register"),
    path('signOut', views.signOut, name="logout"),
    path('createMeeting', views.createMeeting, name='createMeeting'),
    path('joinMeeting', views.joinMeeting, name='joinMeeting'),
]
