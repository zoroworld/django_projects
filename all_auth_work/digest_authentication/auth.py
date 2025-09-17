# digest_authentication/auth.py
import hashlib
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from django.contrib.auth.models import User

# In-memory nonce store
NONCE_STORE = {}

# For testing only: plain-text passwords
PLAIN_PASSWORDS = {
    "auth": "auth",
}

class DigestAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION", "")
        if not auth_header.startswith("Digest "):
            return None

        # Parse header
        auth_data = {}
        try:
            for item in auth_header[7:].split(","):
                key, val = item.strip().split("=", 1)
                auth_data[key] = val.strip('"')
        except Exception:
            raise exceptions.AuthenticationFailed("Malformed Digest header")

        username = auth_data.get("username")
        realm = auth_data.get("realm")
        nonce = auth_data.get("nonce")
        uri = auth_data.get("uri")
        response = auth_data.get("response")

        if not all([username, realm, nonce, uri, response]):
            raise exceptions.AuthenticationFailed("Missing Digest parameters")

        # Fetch user
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("Invalid user")

        # Verify nonce
        if nonce not in NONCE_STORE:
            raise exceptions.AuthenticationFailed("Invalid nonce")

        # Use plain password from PLAIN_PASSWORDS for testing
        password = PLAIN_PASSWORDS.get(username)
        if not password:
            raise exceptions.AuthenticationFailed("Unknown password")

        # Compute HA1 and HA2
        ha1 = hashlib.md5(f"{username}:{realm}:{password}".encode()).hexdigest()
        ha2 = hashlib.md5(f"{request.method}:{uri}".encode()).hexdigest()
        valid_response = hashlib.md5(f"{ha1}:{nonce}:{ha2}".encode()).hexdigest()

        if response != valid_response:
            raise exceptions.AuthenticationFailed("Invalid credentials")

        return (user, None)

    @staticmethod
    def generate_nonce():
        import secrets
        nonce = secrets.token_hex(16)
        NONCE_STORE[nonce] = True
        return nonce

    # calculate hash
    def get_calculated_hash(nonce):
        username = "auth"
        password = "auth"  # matches PLAIN_PASSWORDS
        realm = "MyRealm"
        method = "GET"
        uri = "/secret/"
        nonce = f"{nonce}" # copy from /nonce/

        ha1 = hashlib.md5(f"{username}:{realm}:{password}".encode()).hexdigest()
        ha2 = hashlib.md5(f"{method}:{uri}".encode()).hexdigest()
        response = hashlib.md5(f"{ha1}:{nonce}:{ha2}".encode()).hexdigest()
        return response

    # get curl urls
    def urlsget(nonce, response):
        f"curl http: // 127.0.0.1: 8000 / getkey /"
        user = "auth"
        password = "auth"
        realm = "MyRealm"
        uri = "/secret/"
        nonce = f"{nonce}"
        response = f"{response}"
        host = "http://127.0.0.1:8000/secret/"
        urls = f"curl -i -H 'Authorization: Digest username={user}, realm={realm}, nonce={nonce}, uri={uri}, response={response}' {host} "
        return urls