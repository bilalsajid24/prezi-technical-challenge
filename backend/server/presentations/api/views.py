from rest_framework import filters, generics

from server.presentations.api.serializers import PresentationSerializer
from server.presentations.models import Presentation


class PresentationListAPIView(generics.ListAPIView):
    queryset = Presentation.objects.all()
    serializer_class = PresentationSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["created_at"]
    search_fields = ["title"]
