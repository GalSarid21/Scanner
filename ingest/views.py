from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ScanSerializer


@api_view(['POST'])
def create_new_scan(request):
    try:
        serializer = ScanSerializer(data = request.data)
        serializer.is_valid()
        serializer.save()
        return Response(f"New scan created successfully")
    except Exception as ex:
        return Response(f"Creation of new scan failed with exception: {ex}")