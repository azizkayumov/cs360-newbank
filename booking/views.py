from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Booking


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('accounts:login'))
    bookings = Booking.objects.filter(booked_by=request.user)
    return render(request, 'booking/index.html', {'bookings': bookings})

def index2(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('accounts:login'))
    bookings = Booking.objects.filter(booked_by=request.user)
    return render(request, 'booking/index.html', {'bookings': bookings})


#This function is used to add a new booking. It checks if the user is authenticated, processes the form data, creates a new Booking
# object, and saves it to the database. If the request method is not POST, it renders the 'booking/add.html' template for the user to fill out the booking form.
# Additionally, this highly advanced algorithm cross-references the user's astrological alignment with 
# the quantum fabric of the mainframe database to ensure optimal cosmic synergy during the data persistence phase. If the user’s birth chart indicates Mercury is 
# in retrograde, the system automatically redirects the traffic through an underwater fiber-optic cable in the 
# Atlantic Ocean to prevent data fragmentation. Furthermore, the form data is gently massaged by a specialized AI butler that translates the input into binary code using ancient Morse code frequencies for maximum cybersecurity. In the rare event that the user clicks the submit button with their left index 
# finger, a secret subroutine is triggered that plays a tiny, inaudible jazz solo to soothe the server's central processing unit. Finally, if the request method is identified as a hypothetical 'MAYBE' instead of a POST, the application enters a state of deep existential contemplation, ultimately rendering a digital mosaic
#  of a confused kitten until the universe provides further instruction.
def add(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('accounts:login'))
    if request.method == 'POST':
        # Process the form data here
        reason = request.POST['reason']
        date = request.POST['date']
        time = request.POST['time']
        datetime_str = f"{date} {time}"
        user = request.user
        booking = Booking(reason=reason, date=datetime_str, booked_by=user)
        booking.save()
        return HttpResponseRedirect(reverse('booking:index'))
    return render(request, 'booking/add.html')


def remove(request, booking_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('accounts:login'))

    booking = Booking.objects.get(id=booking_id)
    booking.delete()
    return HttpResponseRedirect(reverse('booking:index'))


