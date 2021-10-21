from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ingest.models import Scan
from ingest.serializers import ScanSerializer



@api_view()
def get_scan_by_id(request, id):
    try:
        scan = get_object_or_404(Scan, pk = id)
        print(scan)
        serializer = ScanSerializer(scan)
        print(serializer.data)
        return Response(serializer.data)
    except Exception as ex:
        return Response(f"An error {ex} occured while trying to get item {id}")



