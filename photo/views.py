from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .models import Photo

# Create your views here.
def photo_list(request):
    return render(request, 'photo/photo_list.html', {})

def login(request):
    request.session['blog_login_sess'] = 'hannal'
    return HttpResponse('[%s] logged in successfully' % request.session['blog_login_sess'])

def logout(request):
    del request.session['blog_login_sess']
    return HttpResponse('logged out successfully')

def signup(request):
    """signup
        to register uesrs
    """
    if request.method == "POST":
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            userform.save()

            return HttpResponseRedirect(
                reverse("signup_ok")
            )

        elif request.method == "GET":
            userform = UserCreationForm()

        return render(request, "registration/signup.html", {
            "userform": userform,
        })