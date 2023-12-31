from rest_framework import serializers


class DAGSerializers(serializers.Serializer):
    id = serializers.IntegerField(allow_null=True)
    name = serializers.CharField(max_length=255)
    create_at = serializers.DateTimeField(allow_null=True, initial=False)
    update_at = serializers.DateTimeField(allow_null=True, initial=False)
    context = serializers.CharField()
    interval = serializers.IntegerField()
    status = serializers.BooleanField(allow_null=True, initial=False)
