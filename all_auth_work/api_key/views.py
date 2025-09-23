from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework_api_key.models import APIKey
from rest_framework.permissions import AllowAny

# Create your views here.
class APIKeyViewSet(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        # You can make name dynamic using request.data if needed
        api_key, key = APIKey.objects.create_key(name="my-unique-key-name")
        return Response({"key": key}, status=status.HTTP_201_CREATED)


class MyProtectedView(APIView):
    permission_classes = [HasAPIKey]

    def get(self, request):
        return Response({"message": "Hello, you have a valid API key!"}, status=status.HTTP_200_OK)


