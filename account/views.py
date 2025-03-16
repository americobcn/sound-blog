from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
        if user is not None:
            if user.is_active:
                login(request, user)
                next_url = request.POST.get("next", request.GET.get("next", "account:dashboard"))
                # return HttpResponse("Authenticated Succesfully")
                return redirect(next, "account:dashboard")
            else:
                return HttpResponse("Diasbled account")

        else:
            return HttpResponse("Invalid Login")

    else:
        form = LoginForm()
        return render(request, "account/login.html", {"form": form})


@login_required
def dashboard(request):
    return render(request, "account/dashboard.html", {"section": "dashboard"})
