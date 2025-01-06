from django.urls import include, path
from rest_framework.routers import DefaultRouter
from stakeholders.views.client import ClientViewSet

router = DefaultRouter()

router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
