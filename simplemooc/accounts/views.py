from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login


def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username, password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('core:index')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)