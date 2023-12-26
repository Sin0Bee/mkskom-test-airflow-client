from django.urls import path, re_path
from dag_generator.views import DAGAPIView, DAGWithIdAPIView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API mkskom-test-airflow-client",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

app_name = "api_v1"
urlpatterns = [
    path('dags', DAGAPIView.as_view()),
    path('dags/<int:pk>', DAGWithIdAPIView.as_view()),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
