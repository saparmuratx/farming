from django.urls import path

from .views import PlotListView

urlpatterns = [
    path("", PlotListView.as_view(), name="plot-list"),
]
