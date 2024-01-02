import datetime

from django.db.models import QuerySet
from rest_framework import generics
from rest_framework.response import Response

from .models import MetaDAG
from .serializers import DAGSerializers
from .utils import DAGManager
from .validator import RequestValidator


class DAGAPIView(generics.GenericAPIView):
    serializer_class = DAGSerializers

    def get(self, request):
        return self._return_items()

    def post(self, request):
        validator = RequestValidator(request=request)
        manager = DAGManager()

        dag_request_object = validator.start()
        result = manager.add(dag_request_object)

        if result['data']['interval'] is None:
            return self._return_items(error=True)

        new_dag = MetaDAG.objects.create(
            name=result['data']['filename'],
            file_path=result['data']['path'],
            context=dag_request_object.context,
            interval=result['data']['interval'],
            update_at=dag_request_object.update_at
        )

        return self._return_items(update=True, new_item=new_dag)

    def _return_items(self, update: bool = None,
                      new_item: QuerySet = None,
                      error: bool = None) -> Response:

        dags = MetaDAG.objects.all()

        if update is not None:
            return Response({"dags": DAGSerializers(dags, many=True).data,
                             "new_dag": DAGSerializers(new_item).data}, status=201)
        elif error is not None:
            return Response({"dags": DAGSerializers(dags, many=True).data}, status=400)
        else:
            return Response({"dags": DAGSerializers(dags, many=True).data}, status=200)


class DAGWithIdAPIView(generics.GenericAPIView):
    serializer_class = DAGSerializers

    def patch(self, request, pk: int) -> Response:
        validator = RequestValidator(request=request)
        manager = DAGManager()

        dag_request_object = validator.start()
        db_obj = MetaDAG.objects.filter(pk=pk)

        update_param = manager.update(filename=dag_request_object.name,
                                      data=dag_request_object,
                                      db_data=db_obj.values()[0])

        if update_param is not None:
            update_param['status'] = False
            update_param['data']['update_at'] = dag_request_object.update_at
            db_obj.update(**update_param['data'])

            return self._return_items()
        else:
            return self._return_items(error=True)

    def delete(self, request, pk: int) -> Response:
        dag_manager = DAGManager()

        db_obj = MetaDAG.objects.filter(pk=pk)
        dag_data = db_obj.values()

        dag_manager.delete(dag_data[0])
        db_obj.delete()

        return self._return_items()

    def _return_items(self, error: bool = None) -> Response:
        dags = MetaDAG.objects.all()

        if error is None:
            return Response({"dags": DAGSerializers(dags, many=True).data}, status=200)
        else:
            return Response({"dags": DAGSerializers(dags, many=True).data}, status=400)
