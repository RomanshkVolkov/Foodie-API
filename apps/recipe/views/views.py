from rest_framework import generics
import os
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.recipe.models.ingredients import Ingredient
from apps.recipe.models.recipe import Category, Recipe, RecipeCategory, Instruction
from apps.recipe.serializers.serializers import CategorySerializer, RecipeSerializer, RecipeGetSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from api_foodie.foodie_finder.main import main


class CategoryListApiView(generics.ListCreateAPIView):
    # queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()


class RecipeDetailView(APIView):
    serializer_class = RecipeGetSerializer

    def get_object(self, pk):
        try:
            return Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        recipe = self.get_object(pk)
        serializer = self.serializer_class(recipe)
        return Response(serializer.data)

    def delete(self, request, pk):
        recipe = self.get_object(pk)
        # image_path = recipe.image.path
        recipe.delete()
        # Elimina la imagen de la receta si existe
        # if os.path.exists(image_path):
        #    os.remove(image_path)
        data = {"message": "Receta eliminada correctamente"}
        return Response(data, status=status.HTTP_204_NO_CONTENT)


class RecipeCreateView(APIView):
    serializer_class = RecipeSerializer
    # parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        ingredient_names = request.data.pop('ingredients')
        ingredients = []
        categoriesList = request.data.pop('categories')
        categories = []
        instructionsList = request.data.pop('instructions')
        instructions = []
        recipe_serializer = self.serializer_class(data=request.data)

        if recipe_serializer.is_valid():
            recipe = recipe_serializer.save()
        else:
            return Response(recipe_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        for ingredient_name in ingredient_names:
            # url = main(ingredient=ingredient_name)
            print(ingredient_name)
            ingredient = Ingredient.objects.create(
                description=ingredient_name['description'], url=ingredient_name['url'], recipe=recipe)
            ingredients.append(ingredient)
            ingredient.save()
        for category in categoriesList:
            cate = RecipeCategory.objects.create(
                recipe=recipe, category=Category.objects.get(id=category))
            categories.append(cate)
            cate.save()

        # print(instructions)
        for instruction in instructionsList:
            print(instruction)
            instructionInstance = Instruction.objects.create(
                description=instruction, recipe=recipe)
            instructionInstance.save()

        data = {"mesage": "Receta creada correctamente"}
        return Response(data, status=status.HTTP_201_CREATED)

    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeGetSerializer(recipes, many=True)
        return Response(serializer.data)
