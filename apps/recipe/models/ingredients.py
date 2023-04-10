from django.db import models
from .recipe import Recipe


class Ingredient(models.Model):
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self):
        return self.description
