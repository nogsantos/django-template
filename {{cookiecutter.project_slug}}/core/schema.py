from graphene import ObjectType
from graphene_federation import build_schema


class Query(ObjectType):
    """Definição da Query usada no Schema."""
    pass


schema = build_schema(query=Query)
