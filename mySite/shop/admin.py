from django.contrib import admin

# Register your models here.
from .models import User

admin.site.register(User)
class userModelAdmin(admin.ModelAdmin):
    list_display = ["id", "user_name", "user_email", "age","additionalInfo","dateOfBirth","profileImage"]