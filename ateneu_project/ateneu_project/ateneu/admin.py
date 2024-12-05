from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'username', 'email', 'is_staff', 'is_active')  # Mostra os campos na lista
    search_fields = ('nome_completo', 'email', 'username')  # Campos para busca
    list_filter = ('is_staff', 'is_active')  # Filtros na lateral
    ordering = ('nome_completo',)  # Ordenação padrão
