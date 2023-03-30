from django.urls import path
from .views import LogIn, SignIn

urlpatterns = [
    # token
    path('login/', LogIn.as_view()),
    path('signIn/', SignIn.as_view(), name='sign_in'),
]
