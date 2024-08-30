from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('about-us/', views.about_us, name='about')
]
