from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.home, name='home'),
    path('leave_table', views.leave_tables, name='leave_table'),
    path('set_email', views.set_email, name='set_email'),

    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('leave/<str:pk>/',views.leave, name='leave'),
    path('create-leave/', views.createleave, name = "create-leave"),
    path('update_leave/', views.update_leave_status, name='update_leave'),

    path('sendEmail/', views.sendEmail, name='emailsomeone')
] 
