from django.contrib import admin
from .models import userAccount, Residence,Unit
# Register your models here.
admin.site.site_header = "Homepower Admin Panel"
admin.site.site_title = "Admin Panel"
admin.site.register(userAccount)
admin.site.register(Residence)
admin.site.register(Unit)