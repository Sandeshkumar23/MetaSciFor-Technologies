from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('hotel/', views.hotel_list, name='hotel_list'),
    path('hotel/<int:hotel_id>/rooms/', views.room_list, name='room_list'),
    path('room/<int:room_id>/book/', views.book_room, name='book_room'),
    path('room/<int:room_id>/add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('apply_coupon/', views.apply_coupon, name='apply_coupon'),
    
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
