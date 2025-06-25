from django.shortcuts import render


def home_view(request):
    user_name = request.GET.get("user_name", "")
    return render(request, "base.html", {"user_name": user_name})
