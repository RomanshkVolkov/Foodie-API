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
