
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.
# Personalizando a exibição do CustomUser no painel admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Campos que serão exibidos na lista de usuários no painel
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active')
    # Campos que serão usados para pesquisa no painel
    search_fields = ('email', 'username', 'first_name', 'last_name')
    # Campos que serão usados no filtro lateral
    list_filter = ('is_staff', 'is_active')
    # Campos que serão exibidos no formulário de edição de um usuário
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # Campos que serão exibidos ao adicionar um novo usuário
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'first_name', 'last_name', 'is_staff', 'is_active'),
        }),
    )
    # Configuração para exibir os campos de forma ordenada
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')

# Registra o modelo CustomUser com o CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
