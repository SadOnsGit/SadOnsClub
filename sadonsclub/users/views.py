from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm

from users.models import CustomUsers


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = CustomUsers.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            return redirect('index:index_page')
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})
        

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Найти пользователя по электронной почте
        try:
            user = CustomUsers.objects.get(email=email)  # Получаем пользователя по email
        except CustomUsers.DoesNotExist:
            user = None  # Если пользователя нет, устанавливаем None

        # Аутентификация пользователя
        if user is not None and user.check_password(password):
            login(request, user)
            return redirect('index:index_page')
        else:
            context = {'error': 'Неправильный адрес электронной почты или пароль.'}
            return render(request, 'login.html', context=context)

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из аккаунта.')
    return redirect('index:index_page')
    
