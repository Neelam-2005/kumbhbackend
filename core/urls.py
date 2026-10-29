from django.urls import path
from . import views

urlpatterns = [
    path('save-booking/', views.save_booking),
    path('get-bookings/', views.get_bookings),

    path('send-otp/', views.send_otp),
    path('verify-otp/', views.verify_otp),
]