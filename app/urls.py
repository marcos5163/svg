from django.urls import path
from app.views import GameViewSet

urlpatterns = [

 path('game/', GameViewSet.as_view({"post":"create", "get": "list"}), name="game_api_view"),
 path('<uuid:game_uuid>/game/', GameViewSet.as_view({"get":"get", "patch": "update", "delete":"delete"}), name="game_api_view"),
  
]