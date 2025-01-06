from rest_framework import serializers, viewsets
from stakeholders.models.client import Client

class ClientSetializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['name']

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSetializer
