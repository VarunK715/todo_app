from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def About(request):
    return render(request,'todoapp/about.html')

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            messages.success(request,f"Your account has been created,You are now able to login.")
            return redirect('login')
        else:
            print(form.errors)
        
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form':form})


def logout_view(request):
    logout(request)
    return render(request,'users/logout.html')

@login_required
def user_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        #print(f"POST - u_form errors: {u_form.errors}, p_form errors: {p_form.errors}")
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f"Your account has been Updated.")
            return redirect('user_profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        print(f"GET - u_form: {u_form}, p_form: {p_form}")

    context={
            'u_form':u_form,
            'p_form':p_form
            }
    return render(request,'users/profile.html',context)

