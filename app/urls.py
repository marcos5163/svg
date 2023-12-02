from django.urls import path
from app.views import GameViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Game CRUD API",
      default_version='v1',
      description="API for managing game records, allowing CRUD operations to create, retrieve, update and delete game information.",
      contact=openapi.Contact(email="marcoschr56@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

 path('game/', GameViewSet.as_view({"post":"create", "get": "list"}), name="game_api_view"),
 path('<uuid:game_uuid>/game/', GameViewSet.as_view({"get":"get", "patch": "update", "delete":"delete"}), name="game_api_view"),
  
]
urlpatterns += [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]