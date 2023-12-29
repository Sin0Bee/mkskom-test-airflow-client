from django.db.models import QuerySet
from rest_framework import generics
from rest_framework.response import Response

from .models import MetaDAG
from .serializers import DAGSerializers
from .utils import DAGManager


class DAGAPIView(generics.GenericAPIView):
    serializer_class = DAGSerializers

    def get(self, request):
        return self._return_items()

    def post(self, request):
        manager = DAGManager()
        result = manager.add(request.data)

        new_dag = MetaDAG.objects.create(
            name=result['data']['filename'],
            file_path=result['data']['path'],
            context=request.data['context'],
            interval=request.data.get('interval', 0)
        )

        return self._return_items(update=True, update_data=new_dag)

    def _return_items(self, update: bool = None, update_data: QuerySet = None) -> Response:
        dags = MetaDAG.objects.all()

        if update is not None:
            return Response({"dags": DAGSerializers(dags, many=True).data,
                             "new_dag": DAGSerializers(update_data).data}, status=201)
        else:
            return Response({"dags": DAGSerializers(dags, many=True).data}, status=200)


class DAGWithIdAPIView(generics.GenericAPIView):
    serializer_class = DAGSerializers

    def patch(self, request, pk: int) -> Response:
        manager = DAGManager()
        qs_obj = MetaDAG.objects.filter(pk=pk)

        update_param = manager.update(filename=request.data['name'], data=request.data, db_data=qs_obj.values()[0])

        if update_param is not None:
            update_param['status'] = False
            qs_obj.update(**update_param['data'])

            return self._return_items()
        else:
            return self._return_items(error=True)

    def delete(self, request, pk: int) -> Response:
        dag_manager = DAGManager()

        qs_obj = MetaDAG.objects.filter(pk=pk)
        dag_data = qs_obj.values()

        dag_manager.delete(dag_data[0])
        qs_obj.delete()

        return self._return_items()

    def _return_items(self, error: bool = False) -> Response:
        dags = MetaDAG.objects.all()

        if error:
            return Response({"dags": DAGSerializers(dags, many=True).data}, status=200)
        else:
            return Response({"dags": DAGSerializers(dags, many=True).data}, status=400)
