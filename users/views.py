from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account creation successful!')
            return redirect('login')
    else:
        form = UserRegisterForm()    
    return render(request, 'users/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')

