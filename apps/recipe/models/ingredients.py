from django.db import models
from .recipe import Recipe


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    recipe_id = models.ForeignKey(
        Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
