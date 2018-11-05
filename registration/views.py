from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
# Create your views here.
def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, 'account created for '+ username)
            form.save() 
            return redirect ('posts')
    else: 
        form = UserRegisterForm()
    return render (request, 'registration/register.html', {'form':form})

@login_required
def profile (request):
    return render(request, 'registration/profile.html')