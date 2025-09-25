from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework_extensions.cache.decorators import cache_response

from api.models import Industry
from api.serializers import IndustrySerializer
from api.permissions import IsAdminOrReadOnly
from api.cache_keys import ListCacheKeyConstructor, DetailCacheKeyConstructor


class IndustryViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    search_fields = ["name"]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    @cache_response(key_func=ListCacheKeyConstructor(), timeout=60 * 10)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @cache_response(key_func=DetailCacheKeyConstructor(), timeout=60 * 10)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
