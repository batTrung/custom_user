from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .forms import CustomUserForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
	add_orm = CustomUserForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = ('username','email','address',)

admin.site.register(CustomUser, CustomUserAdmin)