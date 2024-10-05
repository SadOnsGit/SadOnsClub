from django.urls import path, reverse_lazy
from django.views.generic import CreateView


from . import views
from .forms import RegistrationForm

app_name = 'user'

urlpatterns = [
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=RegistrationForm,
            success_url=reverse_lazy('club:index')
        ),
        name='register'
    ),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('settings/', views.user_settings, name='settings')
]
