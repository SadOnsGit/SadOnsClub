from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import RegistrationForm
from .models import CustomUsers
from bookings.models import Bookings


class RegisterCreateView(CreateView):
    """Представление регистрации пользователя"""
    model = CustomUsers
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('club:index')


def logout_user(request):
    logout(request)
    return redirect('club:index')
    

def profile(request):
    context = {
        'user': get_object_or_404(CustomUsers, username=request.user.username)
    }
    return render(request, 'user/profile.html', context)

def my_bookings(request):
    context = {
        'bookings': Bookings.objects.filter(username_id=request.user.id)
    }
    return render(request, 'user/my_bookings.html', context)

def user_settings(request):
    return render(request, 'user/user_settings.html')