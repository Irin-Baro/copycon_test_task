import requests

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from . import test_data
from .serializers import RequestSerializer


class RequestView(APIView):
    """Представление для выполнения POST запроса
    и извлечения значения поля __name.
    """

    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = RequestSerializer(data=test_data.POST_REQUEST,)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        response = requests.post(
            url=test_data.URL,
            json=data,
            headers={'Authorization': f'Bearer {test_data.TOKEN}'})
        if response.status_code != status.HTTP_200_OK:
            return Response({'error': 'Не удалось получить ответ',
                             'status_code': response.status_code,
                             'response_text': response.text},
                            status=response.status_code)
        try:
            result_data = response.json().get('result', {}).get('result')[0]
            name_field = result_data.get('__name', 'Поле __name отсутствует')
        except (KeyError, IndexError, TypeError):
            name_field = 'Ошибка данных'
        return Response({'__name': name_field}, status=status.HTTP_200_OK)
