from django.urls import include, path
from rest_framework.routers import DefaultRouter
from stakeholders.views.branch_office import BranchOfficeViewSet
from stakeholders.views.client import ClientViewSet

router = DefaultRouter()

router.register(r'clients', ClientViewSet)
router.register(r'branch_offices', BranchOfficeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
