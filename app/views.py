from rest_framework import viewsets
from .models import Game
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.response import Response
from app.serializer import GameSerializer


class GameViewSet(viewsets.ViewSet):
   
   def get(self, request, game_id):
      
      if not Game.objects.filter(id = game_id).exists():
         return Response(status= HTTP_400_BAD_REQUEST, data={"error": "Game not found"})
      
      game = Game.objects.get(id = game_id)

      return Response(status=HTTP_200_OK, data={"name":game.name, "url": game.url, "author": game.author, "publised_date":game.publised_date})
   
   def create(self, request):
      
      serializer = GameSerializer(data= request.data)
      
      if not serializer.is_valid():
         return Response(status=HTTP_400_BAD_REQUEST, data={"error": serializer.errors})
      
      serializer.save()

      return Response(status=HTTP_200_OK, data={"msg": "Created",})
       
   
   def update(self, request, game_id):
      
      if not Game.objects.filter(id = game_id).exists():
         return Response(status= HTTP_400_BAD_REQUEST, data={"error": "Game not found"})

      
      serializer = GameSerializer(data= request.data, instance=Game.objects.get(id = game_id), partial = True)
      
      if not serializer.is_valid():
         return Response(status=HTTP_400_BAD_REQUEST, data={"error": serializer.errors})
      
      serializer.save()

      return Response(status=HTTP_200_OK, data={"msg": "Updated"})
      
   
   def delete(self, request, game_id):
      
      if not Game.objects.filter(id = game_id).exists():
         return Response(status= HTTP_400_BAD_REQUEST, data={"error": "Game not found"})
      
      Game.objects.filter(id = game_id).delete()

      return Response(status=HTTP_200_OK, data={"msg": "Deleted"})

   
   def list(self, request):
      
      data = []
      
      for game in Game.objects.all():
         data.append({"name":game.name, "url": game.url, "author": game.author, "publised_date": game.publised_date})

      return Response(status=HTTP_200_OK, data=data)   
         
  