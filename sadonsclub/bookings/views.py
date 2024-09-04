from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import time

from .models import Computers, Bookings

from users.models import CustomUsers


def booking(request):
    context = {
        'computers': Computers.objects.all()
    }
    return render(request, 'bookings/booking.html', context)

def computer_booking(request, computer_id):
    date_now = timezone.now().date().isoformat()
    available_times = [time(hour=x) for x in range(24)]
    return render(
        request,
        'bookings/computer_booking.html',
        context={
            'id': computer_id,
            'today': date_now,
            'available_times': available_times
        }
    )

def confirm_booking(request, computer_id):
    if request.method == 'POST':
        booked_from = request.POST.get('start_time')
        booked_until = request.POST.get('end_time')
        booking_date = request.POST.get('booking_date')
        user = CustomUsers.objects.get(username=request.user.username)
        computer = get_object_or_404(
            Computers,
            id=computer_id,
            booking=False
        )
        computer.booking = True
        computer.save()
        Bookings.objects.create(
            computer_id=computer,
            username=user,
            booked_from=booked_from,
            booked_until=booked_until,
            booked_to_date=booking_date
        )
    return render(
        request,
        'bookings/confirm_booking.html',
        context={
            'id': computer_id,
            'booking'
            'booked_from': booked_from,
            'booked_until': booked_until,
        }
    )