from rest_framework import viewsets
from api.models import Industry
from api.serializers import IndustrySerializer


class IndustryViewSet(viewsets.ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    search_fields = ["name"]
