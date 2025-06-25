"""
URL configuration for videogamehub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from homepage import views  # importing views from the homepage app

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),  # Default home page (HW8)
    path("games/", views.game_list, name="game_list"),  # List all games
    path(
        "games/<int:game_id>/", views.game_detail, name="game_detail"
    ),  # Show game detail
    # ✅ API endpoints for HW10
    path("api/games/", views.api_all_games, name="api_all_games"),  # All games (GET)
    path(
        "api/game/", views.api_single_game, name="api_single_game"
    ),  # One game by ?id=
    path("api/games/add/", views.api_add_game, name="api_add_game"),  # Add game (POST)
]
