from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from api.serializers import RegisterSerializer, LoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# Signup
class RegisterView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


# Login (JWT)
class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer


# Refresh token
class RefreshTokenView(TokenRefreshView):
    pass
