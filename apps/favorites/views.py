from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from apps.recipe.models.recipe import Favorite
from apps.favorites.serializers import FavoriteSerializer, GetFavoriteSerializer
from apps.recipe.serializers.serializers import RecipeGetSerializer


class FavoritesView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        user = self.request.user
        favorites = Favorite.objects.filter(user=user)
        for favorite in favorites:
            favorite.recipe.favorite = True
        return favorites

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if (self.action == 'create'):
            return FavoriteSerializer
        return GetFavoriteSerializer

    def destroy(self, request, pk=None):
        favorite = self.get_object()
        favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self):
        # favorite = get_object_or_404(Favorite, id=self.kwargs.get('pk'))
        try:
            favorite = Favorite.objects.get(id=self.kwargs.get('pk'))
        except Favorite.DoesNotExist:

            # Si no se encontró, se busca por usuario y receta
            # if not favorite:
            print("entro a ")
            user = self.request.user
            recipe_id = self.kwargs.get('pk')
            favorite = get_object_or_404(
                Favorite, user=user, recipe_id=recipe_id)

        return favorite
