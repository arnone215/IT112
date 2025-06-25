from django.contrib import admin
from .models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "genre", "platform")  # 👈 Custom columns in list view
    search_fields = ("title", "genre")  # 👈 Allows admin to search these fields
    list_filter = ("platform",)  # 👈 Adds a filter sidebar for this field
