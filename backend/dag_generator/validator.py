from datetime import datetime as dt
from dag_generator.models import DAGData


class RequestValidator:
    def __init__(self, request, **kwargs):
        self.kwargs = kwargs
        self.request = request

    def _convert_to_object(self) -> DAGData:
        obj = DAGData(
            pk=self.request.data['id'],
            name=self.request.data['name'],
            context=self.request.data['context'],
            interval=self.request.data['interval'],
            status=self.request.data['status'],
            create_at=self.request.data['create_at'],
            update_at=dt.now()
        )
        return obj

    def start(self):
        return self._convert_to_object()
