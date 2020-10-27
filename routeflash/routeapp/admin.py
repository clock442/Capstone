from django.contrib import admin
from .models import Gym, WallType, HoldType, Route

admin.site.register(Gym)
admin.site.register(WallType)
admin.site.register(HoldType)
admin.site.register(Route)