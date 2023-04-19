from django.urls import path, include

from apps.recipe.views.views import CategoryListApiView, RecipeCreateView, RecipeDetailView

urlpatterns = [
    path('category/', CategoryListApiView.as_view(), name='category'),
    path('', RecipeCreateView.as_view(), name=()),
    path('<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('favorites/', include('apps.favorites.urls'))
]
