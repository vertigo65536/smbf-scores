from django.contrib import admin

# Register your models here.

from .models import Secret, Score, GameStyle, Comms

class SecretAdmin(admin.ModelAdmin):
    list_display = ("name", "value")

class ScoreAdmin(admin.ModelAdmin):
    list_display = ("secret", "p1_tag", "p1_name", "p2_tag", "p2_name", "p1_score", "p2_score", "center_text", "game", "sodium", "banner_flash")

class CommsAdmin(admin.ModelAdmin):
    list_display = ("secret", "p1_name", "p1_sm", "p2_name", "p2_sm", "hidden", "sodium")

class GameStyleAdmin(admin.ModelAdmin):
    list_display = ("game", "style")

admin.site.register(Secret, SecretAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(Comms, CommsAdmin)
admin.site.register(GameStyle, GameStyleAdmin)
