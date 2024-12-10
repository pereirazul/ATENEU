from django.urls import path
from ateneu import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/',views.login_view,name='login'),
    path('cadastro/',views.cadastro,name='cadastro'),
    path('alunos/',views.alunos,name='alunos'),
    path('turmas/',views.turmas,name='turmas')
]