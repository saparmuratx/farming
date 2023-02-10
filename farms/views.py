from rest_framework.generics import ListAPIView
from rest_framework_gis.pagination import GeoJsonPagination

from .serializers import PlotSerializer
from .models import Plot


class PlotListView(ListAPIView):
    queryset = Plot.objects.all()
    pagination_class = GeoJsonPagination
    serializer_class = PlotSerializer
