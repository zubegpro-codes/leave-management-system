from django.contrib import admin
from base.models import CustomUser, Leaves, Location
admin.site.register(CustomUser)
admin.site.register(Leaves)
admin.site.register(Location)
