from rest_framework import serializers


class RequestSerializer(serializers.Serializer):
    """Сериализатор POST запроса."""

    fileHash = serializers.CharField(max_length=256)
    format = serializers.ChoiceField(choices=('xlsx', 'csv', 'json'))
    withEventHandlers = serializers.BooleanField()
