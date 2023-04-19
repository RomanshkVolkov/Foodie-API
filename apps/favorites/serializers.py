from rest_framework import serializers
from apps.recipe.models.recipe import Favorite
from apps.recipe.serializers.serializers import RecipeGetSerializer


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        # fields = '__all__'
        exclude = ['user']

    def validate(self, data):
        # Obtener el usuario y la receta del request
        user = self.context['request'].user
        recipe = data['recipe']

        # Verificar si ya existe un Favorite con el mismo usuario y receta
        if Favorite.objects.filter(user=user, recipe=recipe).exists():
            raise serializers.ValidationError('Esta receta ya es favorita')

        return data


class GetFavoriteSerializer(serializers.ModelSerializer):
    recipe = RecipeGetSerializer()
    exclude = ['user']

    class Meta:
        model = Favorite
        fields = '__all__'
