from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'username', 'email', 'is_staff', 'is_active') 
    search_fields = ('nome_completo', 'email', 'username')  
    list_filter = ('is_staff', 'is_active')  
    ordering = ('nome_completo',)  