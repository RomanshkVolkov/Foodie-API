from rest_framework import serializers
from ..models.recipe import Recipe, Rating, Category, Favorite, Instruction, RecipeCategory
from ..models.ingredients import Ingredient


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

    def to_representation(self, instance):
        # return super().to_representation(instance)
        return {
            "description": instance.description,
            "url": instance.url
        }


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeGetSerializer(serializers.ModelSerializer):
    categories = serializers.StringRelatedField(many=True)
    # ingredients = serializers.StringRelatedField(many=True)
    instructions = serializers.StringRelatedField(many=True)
    ingredients = IngredientSerializer(many=True)
    favorite = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = '__all__'

    def get_favorite(self, obj):
        return obj.favorite


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = '__all__'


class RecipeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeCategory
        fields = '__all__'
