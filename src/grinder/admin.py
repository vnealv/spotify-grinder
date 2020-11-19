from django.contrib import admin

# Register your models here.
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import User


#    "Believe you can and you're halfway there."
#              ~Theodore Roosevelt~

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'username']

admin.site.register(User, CustomUserAdmin)
