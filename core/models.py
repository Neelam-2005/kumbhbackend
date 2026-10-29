from django.db import models

class CrowdStatus(models.Model):
    ghat_name = models.CharField(max_length=100)
    level = models.CharField(max_length=20)

    def __str__(self):
        return self.ghat_name + " - " + self.level


class Stay(models.Model):
    hotel_name = models.CharField(max_length=200)
    normal_price = models.IntegerField()
    peak_price = models.IntegerField()
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.hotel_name


class Booking(models.Model):
    name = models.CharField(max_length=100)
    hotel = models.CharField(max_length=200)
    days = models.IntegerField()
    people = models.IntegerField()
    room_type = models.CharField(max_length=50)
    booking_date = models.DateField()
    total = models.IntegerField()

    def __str__(self):
        return self.name + " - " + self.hotel


class LostReport(models.Model):
    item_name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.item_name


# NEW OTP MODEL
class OTP(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email + " - " + self.otp