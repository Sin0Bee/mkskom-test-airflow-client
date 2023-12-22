from rest_framework import serializers


class DAGSerializers(serializers.Serializer):
    id = serializers.IntegerField(allow_null=True)
    name = serializers.CharField(max_length=255)
    file_path = serializers.CharField(allow_blank=True)
    create_at = serializers.DateTimeField(allow_null=True)
    update_at = serializers.DateTimeField(allow_null=True)
    context = serializers.CharField()
    interval = serializers.IntegerField()

