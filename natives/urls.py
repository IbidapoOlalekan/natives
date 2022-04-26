from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('natives', views.NativeViewSet)
router.register('cohort', views.CohortViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]