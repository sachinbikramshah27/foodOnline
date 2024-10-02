from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


# Register your models here.

class CustomUserAdmin(UserAdmin):


    fieldsets = ()
    filter_horizontal=()
   # filter_vertical=()
    list_filter = ()
    list_display=['email','first_name','last_name','username','role','is_admin']
    ordering = ['-joined_date']

    

    


admin.site.register(models.User, CustomUserAdmin)
admin.site.register(models.UserProfile)