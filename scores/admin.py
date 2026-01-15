from django.contrib import admin

# Register your models here.

from .models import Secret, Score, GameStyle

class SecretAdmin(admin.ModelAdmin):
    list_display = ("name", "value")

class ScoreAdmin(admin.ModelAdmin):
    list_display = ("secret", "p1_tag", "p1_name", "p2_tag", "p2_name", "p1_score", "p2_score", "center_text", "game")

class GameStyleAdmin(admin.ModelAdmin):
    list_display = ("game", "style")

admin.site.register(Secret, SecretAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(GameStyle, GameStyleAdmin)
