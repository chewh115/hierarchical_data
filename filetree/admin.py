from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Files

# Register your models here.
admin.site.register(Files, DraggableMPTTAdmin)