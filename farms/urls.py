from django.urls import path

from .views import PlotView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r"plots", PlotView)

urlpatterns = router.urls
