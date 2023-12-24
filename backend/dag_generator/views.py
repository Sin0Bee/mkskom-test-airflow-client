from rest_framework.response import Response
from rest_framework.views import APIView

from airflow_api.airflow import AirflowAPI
from .models import MetaDAG
from .serializers import DAGSerializers
from .utils import DAGManager


class DAGListAPIView(APIView):

    def get(self, request):
        dags = MetaDAG.objects.all()
        return Response({"dags": DAGSerializers(dags, many=True).data,
                         "status": "success",
                         "status_code": 200})


class AddDAG(APIView):
    def post(self, request):
        manager = DAGManager()
        result = manager.add(request.data)

        new_dag = MetaDAG.objects.create(
            name=result['data']['filename'],
            file_path=result['data']['path'],
            context=request.data['context'],
            interval=request.data.get('interval', 0)
        )

        return Response({"dags": DAGSerializers(MetaDAG.objects.all(), many=True).data,
                         "new_dag": DAGSerializers(new_dag).data,
                         "status": "success",
                         "status_code": 201})


class UpdateDAG(APIView):
    def patch(self, request):

        MetaDAG.objects.filter(pk=request.data['id']).update(**request.data['update_param'])

        dags = MetaDAG.objects.all()

        return Response({"dags": DAGSerializers(dags, many=True).data,
                         "status": "success",
                         "status_code": 200
                         })


class DeleteDAG(APIView):
    def delete(self, request):
        dag_manager = DAGManager()

        MetaDAG.objects.filter(pk=request.data['id']).delete()
        dag_manager.delete(request.data)
        dags = MetaDAG.objects.all()

        return Response({"dags": DAGSerializers(dags, many=True).data,
                         "status": "success",
                         "status_code": 200
                         })
