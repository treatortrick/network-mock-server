import time
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

from .models.mock_models import MockResponse


class MockView(APIView):
    
    def mock_response(self, request, url, *args, **kwargs):
        method = request.method
        url = '/'+url if not url.startswith('/') else url
        try:
            mock_response = MockResponse.objects.get(url=url, request_method=method, is_deleted=False, enable=True)
            time.sleep(mock_response.delay_seconds)
            return Response(mock_response.response_data)
        except MockResponse.DoesNotExist:
            return Response({'error': 'Mock API not found'}, status=500)
    
    def get(self, request, *args, **kwargs):
        return self.mock_response(request, url=kwargs.pop('url') )

    def post(self, request, *args, **kwargs):
        return self.mock_response(request, url=kwargs.pop('url') )

    def put(self, request, *args, **kwargs):
        return self.mock_response(request, url=kwargs.pop('url') )

    def delete(self, request, *args, **kwargs):
        return self.mock_response(request, url=kwargs.pop('url') )