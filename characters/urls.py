from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='home-homepage'),
    path('characters/', views.characters, name='characters'),
    path('characters/details/<str:name>/', views.characters_details, name='char-detail'),
    path('summary/', views.summary_view, name='summary-view'),
    path('play/', views.game_view, name='game-view'),
    path('play/game', views.game_play_view, name='real-game')
]
