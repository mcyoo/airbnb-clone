from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin """

    #list_display = ("username","email","gender","langauge")
    #list_filter = ("langauge","currency","superhost")
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile", 
            {
                "fields": (
                    "gender",
                    "avator",
                    "bio",
                    "birthdate",
                    "langauge",
                    "currency",
                    "superhost",
                ),
            }   
        ),
    )
    