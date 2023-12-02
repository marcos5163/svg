from rest_framework import viewsets
from .models import Game
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.response import Response
from app.serializer import GameSerializer
from django.core.paginator import Paginator


class GameViewSet(viewsets.ViewSet):
   
   def get(self, request, game_uuid):
      
      if not Game.objects.filter(uuid = game_uuid).exists():
         return Response(status= HTTP_400_BAD_REQUEST, data={"error": "Game not found"})
      
      game = Game.objects.get(uuid = game_uuid)

      return Response(status=HTTP_200_OK, data=GameSerializer(game).data)
   
   def create(self, request):
      
      serializer = GameSerializer(data= request.data)
      
      if not serializer.is_valid():
         return Response(status=HTTP_400_BAD_REQUEST, data={"error": serializer.errors})
      
      serializer.save()


      return Response(status=HTTP_200_OK, data={"msg": "Created"})
       
   
   def update(self, request, game_uuid):
      
      if not Game.objects.filter(uuid = game_uuid).exists():
         return Response(status= HTTP_400_BAD_REQUEST, data={"error": "Game not found"})

      
      serializer = GameSerializer(data= request.data, instance=Game.objects.get(uuid = game_uuid), partial = True)
      
      if not serializer.is_valid():
         return Response(status=HTTP_400_BAD_REQUEST, data={"error": serializer.errors})
      
      serializer.save()

      return Response(status=HTTP_200_OK, data={"msg": "Updated"})
      
   
   def delete(self, request, game_uuid):
      
      if not Game.objects.filter(uuid = game_uuid).exists():
         return Response(status= HTTP_400_BAD_REQUEST, data={"error": "Game not found"})
      
      Game.objects.filter(id = game_uuid).delete()

      return Response(status=HTTP_200_OK, data={"msg": "Deleted"})

   
   def list(self, request):
      
      data = []

      game_queryset = Game.objects.all()
      
      page_size = int(request.query_params.get('page_size', '20'))
      page = int(request.query_params.get('page', '1'))

      
      paginator = Paginator(game_queryset, page_size)

      # for game in paginator.get_page(page):
      #    data.append({"id": game.id, "name":game.name, "url": game.url, "author": game.author, "publised_date": game.publised_date})

      return Response(status=HTTP_200_OK, data=GameSerializer(paginator.get_page(page), many=True).data)   
         
  