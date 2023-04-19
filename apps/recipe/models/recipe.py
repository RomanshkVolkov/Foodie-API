from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField(null=True, blank=True, max_length=500)
    preparation_time = models.CharField(max_length=20, null=True)
    categories = models.ManyToManyField(Category, through='RecipeCategory')

    class Meta:
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'

    def __str__(self):
        return self.title


class Rating(models.Model):
    score = models.IntegerField()
    comment = models.CharField(max_length=255)
    recipe = recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='ratings')

    class Meta:
        verbose_name = 'valoracion'
        verbose_name_plural = 'valoraciones'

    def __str__(self):
        return self.score


class Instruction(models.Model):
    description = models.TextField()
    recipe = recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='instructions')

    class Meta:
        verbose_name = 'instrucion'
        verbose_name_plural = 'instrucciones'

    def __str__(self):
        return self.description


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.category


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'recipe')
