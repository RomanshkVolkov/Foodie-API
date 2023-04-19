from rest_framework import viewsets, permissions
from apps.recipe.models.recipe import Favorite
from apps.favorites.serializers import FavoriteSerializer


class FavoritesView(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FavoriteSerializer
