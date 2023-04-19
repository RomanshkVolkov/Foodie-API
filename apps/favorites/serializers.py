from rest_framework import serializers
from apps.recipe.models.recipe import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
