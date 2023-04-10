from .views import MyView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('apps.auth.urls')),
    path('foodie-finder/', MyView.as_view(), name='foodie-finder'),
    path('recipe/', include('apps.recipe.urls'), name='recipe')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
