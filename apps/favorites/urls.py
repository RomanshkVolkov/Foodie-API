from rest_framework import routers
from .views import FavoritesView

router = routers.DefaultRouter()

router.register('', FavoritesView, 'favorites')

urlpatterns = router.urls
