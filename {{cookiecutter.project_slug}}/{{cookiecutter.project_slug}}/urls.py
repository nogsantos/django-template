from django.urls import path, include
{% if cookiecutter.use_graphql == "y" -%}
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
{%- endif %}


urlpatterns = [
    path('api/v1/', include('core.urls'), name='core'),
    {% if cookiecutter.use_graphql == "y" -%}
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    {%- endif %}
]
