from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from api.serializers import RegisterSerializer


# Signup
class RegisterView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
