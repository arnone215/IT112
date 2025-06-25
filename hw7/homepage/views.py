# Create your views here.
from django.shortcuts import render
from .models import Game
from django.shortcuts import get_object_or_404


def home(request):
    user_name = request.GET.get("user_name")
    return render(request, "base.html", {"user_name": user_name})


def game_list(request):
    games = Game.objects.all()
    return render(request, "game_list.html", {"games": games})


def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, "game_detail.html", {"game": game})
