from rest_framework.viewsets import ModelViewSet
from rest_framework_gis.pagination import GeoJsonPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import PlotSerializer
from .models import Plot
from .permissions import IsAuthorOrReadOnly


class PlotView(ModelViewSet):
    queryset = Plot.objects.all()
    pagination_class = GeoJsonPagination
    serializer_class = PlotSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly,
    )

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Plot.objects.all()
        return Plot.objects.filter(farmer=user)
