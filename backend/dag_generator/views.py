from django.db.models import QuerySet
from rest_framework import generics
from rest_framework.response import Response

from .models import MetaDAG, DAGData
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

    def _return_items(self, update: bool = None, update_data: QuerySet = None):
        dags = MetaDAG.objects.all()

        if update is not None:
            return Response({"dags": DAGSerializers(dags, many=True).data,
                         "new_dag": DAGSerializers(update_data).data,
                         "status": "success",
                         "status_code": 201})
        else:

            return Response({"dags": DAGSerializers(dags, many=True).data,
                         "status": "success",
                         "status_code": 200})


class DAGWithIdAPIView(generics.GenericAPIView):

    serializer_class = DAGSerializers

    def patch(self, request, pk: int):
        manager = DAGManager()

        request.data['update_param']['status'] = False

        MetaDAG.objects.filter(pk=pk).update(**request.data['update_param'])
        manager.update(filename=request.data['name'], data=request.data)

        return self._return_items()

    def delete(self, request, pk: int):
        dag_manager = DAGManager()

        qs_obj = MetaDAG.objects.filter(pk=pk)
        dag_data = qs_obj.values()

        del_status = dag_manager.delete(dag_data[0])
        qs_obj.delete()

        return self._return_items()

    def _return_items(self):
        dags = MetaDAG.objects.all()

        return Response({"dags": DAGSerializers(dags, many=True).data,
                         "status": "success",
                         "status_code": 200
                         })
