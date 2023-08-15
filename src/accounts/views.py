

from django.shortcuts import redirect, render

from accounts.forms import UserRegistration


def profile(request):
    template_name = 'accounts/profile.html'
    context = {
        'session': 'profile',
    }
    return render(request, template_name, context)


def register(request):    
    if request.method == 'POST':
        user_form = UserRegistration(request.POST)
        if user_form.is_valid:
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        user_form = UserRegistration()
    
    return render(request, 'accounts/registration.html', {'user_form': user_form})