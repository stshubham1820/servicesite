from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(contact_us)

admin.site.register(about_us)

admin.site.register(service_category)

admin.site.register(service_sub_category)

admin.site.register(testimonials)

admin.site.register(feedback)