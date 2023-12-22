from django.urls import path
from dag_generator.views import DAGListAPIView, AddDAG, UpdateDAG, DeleteDAG

app_name = "api_v1"
urlpatterns = [
    path('get_dags', DAGListAPIView.as_view()),
    path('add_dag', AddDAG.as_view()),
    path('update_dag', UpdateDAG.as_view()),
    path('delete_dag', DeleteDAG.as_view()),
]
