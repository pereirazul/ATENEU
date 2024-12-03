from django.urls import path
from ateneu import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/',views.login,name='login'),
    path('cadastro/',views.cadastro,name='cadastro')
]