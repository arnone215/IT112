from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def home(request):
    user_name = request.GET.get("user_name")
    return render(request, "base.html", {"user_name": user_name})
