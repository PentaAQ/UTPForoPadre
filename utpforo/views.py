from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def logear(request):
    if request.method == 'POST':
        username = request.POST['codigoutp']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html', {})

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('logear')



