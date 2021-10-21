from rest_framework import serializers
from ingest.models import Scan


class ScanSerializer(serializers.Serializer):
    class Meta:
        model = Scan
        fields = ['id', 'status', 'creation_time']
    
    def create(self, validated_data):
        scan = Scan(**validated_data)
        scan.save()
        return scan
    