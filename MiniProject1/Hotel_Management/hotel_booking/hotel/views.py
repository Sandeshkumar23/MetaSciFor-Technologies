from django.shortcuts import render, get_object_or_404, redirect
from .models import Hotel, Room, Booking, Cart, Coupon
from django.db.models import Q

from django.shortcuts import render
from .models import Hotel

from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def dashboard(request):
    # Fetch all hotels for the dashboard
    hotels = Hotel.objects.all()
    return render(request, 'registration/dashboard.html', {'hotels': hotels})


@login_required
def hotel_list(request):
    # Get 'state' and 'rating' from GET request
    state = request.GET.get('state')
    rating = request.GET.get('rating')

    # Start with all hotels
    hotels = Hotel.objects.all()

    # Filter hotels by state if provided
    if state:
        hotels = hotels.filter(state__icontains=state)

    # Filter hotels by rating if provided
    if rating:
        hotels = hotels.filter(rating__gte=rating)

    # Pass filtered hotels to the template
    return render(request, 'hotel/hotel_list.html', {'hotels': hotels})



def room_list(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    rooms = Room.objects.filter(hotel=hotel, is_available=True)
    return render(request, 'hotel/room_list.html', {'hotel': hotel, 'rooms': rooms})

def book_room(request, room_id):
    if request.method == 'POST':
        room = get_object_or_404(Room, id=room_id)
        customer_name = request.POST.get('customer_name')
        check_in_date = request.POST.get('check_in_date')
        check_out_date = request.POST.get('check_out_date')
        total_amount = room.price * ((check_out_date - check_in_date).days)

        Booking.objects.create(
            customer_name=customer_name,
            room=room,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            total_amount=total_amount
        )
        return redirect('hotel_list')
    return render(request, 'hotel/book_room.html')

def add_to_cart(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    cart, created = Cart.objects.get_or_create(customer_name=request.user.username)
    cart.rooms.add(room)
    return redirect('hotel_list')

def view_cart(request):
    cart = Cart.objects.get(customer_name=request.user.username)
    return render(request, 'hotel/view_cart.html', {'cart': cart})

def apply_coupon(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        coupon = Coupon.objects.filter(code=code, is_active=True).first()
        if coupon:
            # Apply the coupon logic
            return redirect('view_cart')
    return render(request, 'hotel/apply_coupon.html')

