
def usersignup(request):
    if request.method == "POST":
        form = SignUPForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignUPForm()

    return render(request, "signup.html", {"form": form})


def userlogin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("mainpage")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})
