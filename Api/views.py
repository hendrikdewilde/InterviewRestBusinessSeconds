import logging

from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from Api.classes import APIRootMetadata
from Api.serializers import BusinessSecondsSerializer

log = logging.getLogger(__name__)


class BusinessSecondsViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
    serializer_class = BusinessSecondsSerializer
    http_method_names = ['get', 'head', 'options']
    metadata_class = APIRootMetadata

    def list(self, request, format=None):
        serializer = self.serializer_class(data=request.query_params,
                                           context={'request': request})
        serializer.validate(request.query_params)

        serializer.is_valid(raise_exception=True)
        if serializer.validated_data:
            start_time = serializer.validate_content(request.query_params['start_time'])
            end_time = serializer.validate_content(request.query_params['end_time'])
            if start_time and end_time:
                seconds = serializer.count_business_seconds(start_time, end_time)
                return Response({'seconds': seconds})
            else:
                return Response(serializer.errors.values(), status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors.values(), status=status.HTTP_400_BAD_REQUEST)
