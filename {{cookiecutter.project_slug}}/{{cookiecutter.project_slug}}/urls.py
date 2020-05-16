from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
{% if cookiecutter.use_graphql == "y" -%}
from django.views.decorators.csrf import csrf_exempt
from graphene_sentry.views import SentryGraphQLView
{%- endif %}

schema_view = get_schema_view(
    openapi.Info(
        title='{{ cookiecutter.project_name }} API',
        description='{{ cookiecutter.description }} API',
        default_version='v1',
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    path('', include('core.urls'), name='core'),
    {% if cookiecutter.use_graphql == "y" -%}
    path('graphql/', csrf_exempt(SentryGraphQLView.as_view(graphiql=True))),
    {%- endif %}
]
