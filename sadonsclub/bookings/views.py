from django.shortcuts import render

from .models import Computers

def booking(request):
    context = {
        'computers': Computers.objects.all()
    }
    return render(request, 'bookings/booking.html', context)