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


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeGetSerializer(serializers.ModelSerializer):
    categories = serializers.StringRelatedField(many=True)
    ingredients = serializers.StringRelatedField(many=True)
    instructions = serializers.StringRelatedField(many=True)

    class Meta:
        model = Recipe
        fields = '__all__'


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
