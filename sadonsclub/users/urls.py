from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('register/', views.RegisterCreateView.as_view(), name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('settings/', views.user_settings, name='settings')
]
