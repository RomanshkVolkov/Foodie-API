from django.contrib import admin
from .models.recipe import Category, Favorite, Instruction, Rating, Recipe, RecipeCategory
from .models.ingredients import Ingredient

admin.site.register(Category)
admin.site.register(Favorite)
admin.site.register(Instruction)
admin.site.register(Rating)
admin.site.register(Recipe)
admin.site.register(RecipeCategory)
admin.site.register(Ingredient)
# Register your models here.
