from rest_framework_gis import serializers

from .models import Plot


class PlotSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = Plot
        geo_field = "contour"
        fields = (
            "id",
            "farmer",
            "culture",
            "season",
        )
