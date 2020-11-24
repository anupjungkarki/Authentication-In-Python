from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm, ProfileForm, ProfileModelForm


# Create your views here.
def index(request):
    return render(request, "index.html")


def RegisterUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # data = form.cleaned_data /Case of Register Through through Model
            # user = User.objects.create(username=data['username'])
            # user.set_password(data['password1'])
            # user.save()
            return redirect('/')

    form = UserCreationForm()
    context = {'form': form}
    return render(request, "register.html", context)


def UserLogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
    form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)


@login_required  # It will Not give access to page if user is not login
def content(request):
    return render(request, 'content.html')


def LogoutUser(request):
    logout(request)
    return redirect('/')


@login_required
def UserProfile(request):
    if request.method == 'POST':
        profile_form = ProfileModelForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
        data = request.POST
        first_name = data['first_name']
        last_name = data['last_name']
        user_data = User.objects.get(id=request.user.id)
        user_data.first_name = first_name
        user_data.last_name = last_name
        user_data.save()
        return redirect('/profile')
    form = ProfileForm(initial=
                       {'first_name': request.user.first_name,
                        'last_name': request.user.last_name
                        })
    profile_form = ProfileModelForm(initial={'image': request.user.profile.image.url})
    context = {'form': form, 'profile_form': profile_form}
    return render(request, "profile.html", context)
