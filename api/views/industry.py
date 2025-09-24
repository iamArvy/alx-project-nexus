from rest_framework import viewsets
from api.models import Industry
from api.serializers import IndustrySerializer
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsAdminOrReadOnly


class IndustryViewSet(viewsets.ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    search_fields = ["name"]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
