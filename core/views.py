from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random
from datetime import datetime

from .models import Booking, OTP


@csrf_exempt
def save_booking(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            Booking.objects.create(
                name=data.get("name"),
                hotel=data.get("hotel"),
                days=int(data.get("days")),
                people=int(data.get("people")),
                room_type=data.get("roomType"),
                booking_date=data.get("booking_date"),
                total=int(data.get("total"))
            )

            return JsonResponse({"status": "success"})

        except Exception as e:
            print("ERROR:", e)
            return JsonResponse({"status": "failed"})

    return JsonResponse({"message": "POST request required"})


def get_bookings(request):
    bookings = list(Booking.objects.values())
    return JsonResponse(bookings, safe=False)


# ================= OTP SYSTEM ================= #

# SEND OTP (DUMMY - PRINT IN TERMINAL)
@csrf_exempt
def send_otp(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email")

            otp = str(random.randint(100000, 999999))

            OTP.objects.create(email=email, otp=otp)

            # 🔥 PRINT OTP IN TERMINAL (FOR DEMO)
            print("\n===================================")
            print(f"OTP for {email} is: {otp}")
            print("===================================\n")

            return JsonResponse({"status": "otp_sent"})

        except Exception as e:
            print("ERROR:", e)
            return JsonResponse({"status": "failed"})

    return JsonResponse({"message": "POST request required"})


# VERIFY OTP
@csrf_exempt
def verify_otp(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email")
            otp_entered = data.get("otp")

            otp_obj = OTP.objects.filter(email=email).last()

            if otp_obj:
                # Expiry check (5 minutes)
                if datetime.now().timestamp() - otp_obj.created_at.timestamp() > 300:
                    return JsonResponse({"status": "expired"})

                if otp_obj.otp == otp_entered:
                    return JsonResponse({"status": "verified"})

            return JsonResponse({"status": "invalid_otp"})

        except Exception as e:
            print("ERROR:", e)
            return JsonResponse({"status": "failed"})

    return JsonResponse({"message": "POST request required"})