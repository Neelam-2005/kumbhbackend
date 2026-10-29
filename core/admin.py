from django.contrib import admin
from .models import Stay, Booking, CrowdStatus, LostReport

admin.site.register(Stay)
admin.site.register(Booking)
admin.site.register(CrowdStatus)
admin.site.register(LostReport)
