from django.urls import path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework import renderers
from django.conf import settings

SETTINGS = getattr(settings, 'DRFSWAGGER', {
   'API_TITLE': 'API'
})

app_name = 'drfswagger'

urlpatterns = [
    path('', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'drfswagger:openapi-schema-yaml'}
    ), name='swagger-ui'),
    path('openapi.yaml', get_schema_view(
            title=SETTINGS['API_TITLE'],
            renderer_classes=[renderers.OpenAPIRenderer]
        ), name='openapi-schema-yaml'),
    path('openapi.json', get_schema_view(
            title=SETTINGS['API_TITLE'],
            renderer_classes = [renderers.JSONOpenAPIRenderer],
        ), name='openapi-schema-json'),
]
