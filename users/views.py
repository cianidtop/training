from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('home-main')
    else:
            form = UserCreationForm()
    form = UserCreationForm()
    return render(request, 'users/registration.html', {'form': form, 'title': 'Регистрация пользователя'})
