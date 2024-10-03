from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100, default='Default Name')
    address = models.TextField(max_length=100, default='Default Name')
    city = models.CharField(max_length=50, default='Default City')
    state = models.CharField(max_length=50, default='Default State')
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=3.0)  # Default value set here
  

    def __str__(self):
        return self.name

class Room(models.Model):

    ROOM_TYPE_CHOICES = [
        ('deluxe', 'Deluxe'),
        ('super_deluxe', 'Super Deluxe'),
        ('suite', 'Suite'),
    ]

    hotel = models.ForeignKey(Hotel, related_name='rooms', on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50, choices=ROOM_TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.room_number} in {self.hotel.name}"

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Booking by {self.customer_name} for {self.room}"

class Cart(models.Model):
    customer_name = models.CharField(max_length=100)
    rooms = models.ManyToManyField(Room)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Cart {self.id} for {self.user.username}"

class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)  # Discount as percentage
    is_active = models.BooleanField(default=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} x {self.room.room_number} ({self.room.room_type})"