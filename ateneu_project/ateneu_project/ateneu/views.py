from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse

def sobre(request):
    html = '<html lang="pt-br"><body><h1>Alô mundo</h1></body></html>'
    return HttpResponse(html)

def home(request):
    return render(request, '../public/index.html')
def cadastro(request):
    return render(request,'../public/cadastro.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Usuário ou senha inválidos')
    return render(request,'../public/login.html')

#def delete_item(request, item_id):
    #if request.method == 'DELETE':
    # lógica para deletar item...
    #return HttpResponse('Item deletado', status=204)
    