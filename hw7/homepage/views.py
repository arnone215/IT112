# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # <-- ✅ Add this line
from .models import Game
import json


def home(request):
    user_name = request.GET.get("user_name")
    return render(request, "base.html", {"user_name": user_name})


def game_list(request):
    games = Game.objects.all()
    return render(request, "game_list.html", {"games": games})


def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, "game_detail.html", {"game": game})


# 🌐 API: Get all games as JSON
def api_all_games(request):
    games = Game.objects.all()
    game_data = list(games.values())  # Converts queryset to list of dicts
    return JsonResponse(game_data, safe=False, content_type="application/json")


# 🌐 API: Get one game based on ?id=<game_id>
def api_single_game(request):
    game_id = request.GET.get("id")
    if game_id is None:
        return JsonResponse(
            {"error": "Missing game id"}, status=200, content_type="application/json"
        )

    game = Game.objects.filter(id=game_id).values().first()
    if game is None:
        return JsonResponse(
            {"error": "Game not found"}, status=200, content_type="application/json"
        )

    return JsonResponse(game, safe=False, content_type="application/json")


# 🌐 API: Create new game with POST data
@csrf_exempt  # <-- ✅ Add this decorator
def api_add_game(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            title = data.get("title")
            genre = data.get("genre")
            platform = data.get("platform")

            if not title or not genre or not platform:
                return JsonResponse(
                    {"error": "Missing fields in request"},
                    status=200,
                    content_type="application/json",
                )

            new_game = Game.objects.create(title=title, genre=genre, platform=platform)
            return JsonResponse(
                {"success": f'Game "{new_game.title}" added successfully'},
                status=200,
                content_type="application/json",
            )

        except json.JSONDecodeError:
            return JsonResponse(
                {"error": "Invalid JSON"}, status=200, content_type="application/json"
            )

    return JsonResponse(
        {"error": "Only POST requests allowed"},
        status=200,
        content_type="application/json",
    )
