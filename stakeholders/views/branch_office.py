from rest_framework import serializers, viewsets

from stakeholders.models.branch_office import BranchOffice

class BranchOfficeSetializer(serializers.ModelSerializer):
    class Meta:
        model = BranchOffice
        fields = ['name']

class BranchOfficeViewSet(viewsets.ModelViewSet):
    queryset = BranchOffice.objects.all()
    serializer_class = BranchOfficeSetializer
