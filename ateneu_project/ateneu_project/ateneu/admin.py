from django.contrib import admin

# Register your models here.
@adminregister(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets= UserAdmin.fieldsets+(
        (None,{'fields':('email','senha')}),
    )