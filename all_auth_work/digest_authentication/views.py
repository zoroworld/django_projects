from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .auth import DigestAuthentication


# Digest-protected API view
class SecretView(APIView):
    authentication_classes = [DigestAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello {request.user.username}, this is protected!"})

# Endpoint to generate a nonce
def get_auth(request):
    nonce = DigestAuthentication.generate_nonce()
    calculated_hash = DigestAuthentication.get_calculated_hash(nonce)
    get_data = DigestAuthentication.urlsget(nonce, calculated_hash)
    return JsonResponse({"urls": get_data})

