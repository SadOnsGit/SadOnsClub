from django.urls import path

from . import views


app_name = 'bookings'

urlpatterns = [
    path('', views.booking, name='booking'),
    path('computer_booking/<int:computer_id>/', views.computer_booking, name='computer_booking'),
    path(
        'computer_booking/<int:computer_id>/confirm_booking',
        views.confirm_booking,
        name='confirm_booking'
    )
]
