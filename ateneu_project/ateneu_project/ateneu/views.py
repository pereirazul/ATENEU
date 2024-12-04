from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()

def home(request):
    return render(request, '../public/index.html')

def cadastro(request):
    if request.method == 'POST':  # Verifica se é uma requisição POST
        email = request.POST.get('username')  # Obtém o email do formulário
        password = request.POST.get('password')  # Obtém a senha do formulário

        # Verifica se o usuário já existe
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Usuário já existe.')
        else:
            # Cria um novo usuário
            user = User.objects.create_user(username=email, email=email, password=password)
            messages.success(request, 'Usuário cadastrado com sucesso! Faça login.')
            return redirect('login')  # Redireciona para a página de login

    return render(request, '../public/cadastro.html')  # Renderiza o template de cadastro

def login_view(request):  # Renomeei a função para evitar conflito com a função `login` do Django
    if request.method == 'POST':  # Verifica se é uma requisição POST
        username = request.POST['username']  # Obtém o nome de usuário do formulário
        password = request.POST['password']  # Obtém a senha do formulário
        user = authenticate(request, username=username, password=password)  # Autentica o usuário
        if user is not None:
            auth_login(request, user)  # Usa a função `login` do Django, renomeada como `auth_login`
            return redirect('home')  # Redireciona para a página inicial
        else:
            messages.error(request, 'Usuário ou senha inválidos')  # Exibe mensagem de erro

    return render(request, '../public/login.html')  # Renderiza o template de login
