from django.contrib import admin
from game.models import Game, Player, Card, Hand, Pool

class GameAdmin(admin.ModelAdmin):
    list_display = ('gameLobbyID', 'numOfPlayers', 'score')

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('gameLobbyID', 'playerID', 'displayName')

class CardAdmin(admin.ModelAdmin):
    list_display = ('cardID')

class HandAdmin(admin.ModelAdmin):
    list_display = ('playerID', 'cardID')

class PoolAdmin(admin.ModelAdmin):
    list_display = ('cardID')

admin.site.register(Game, GameAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Hand, HandAdmin)
admin.site.register(Pool, PoolAdmin)

