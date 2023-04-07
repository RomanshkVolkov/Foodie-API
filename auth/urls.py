from django.urls import path
from .views import LogIn, SignUp

urlpatterns = [
    # token
    path('login/', LogIn.as_view(), name='login'),
    path('signup/', SignUp.as_view(), name='signup'),
]
