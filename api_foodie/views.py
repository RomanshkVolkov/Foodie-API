from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import MySerializer
from .foodie_finder.main import main
from django.http import JsonResponse


class MyView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        serializer = MySerializer(data=request.query_params)
        if serializer.is_valid():
            response = serializer.to_representation(None)
            ingredient_url = main(response['search'], response['training_mode'])
            data = {'url': ingredient_url}
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
