from django.urls import path
from ateneu import views

urlpatterns = [
    path('sobre/', views.sobre, name='sobre'),
    path('home/', views.home, name='home'),
    path('login/',views.login,name='login')
]