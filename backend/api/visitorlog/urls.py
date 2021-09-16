from django.urls import include, path

from rest_framework import routers

from visitorlog.views import LogViewSet

router = routers.DefaultRouter()
router.register(r'logs', LogViewSet)

urlpatterns = [
   path('', include(router.urls)),
]