from graphene import ObjectType
from graphene_federation import build_schema


class Query(ObjectType):
    """Schema queries definitions

    Arguments:
        ObjectType {[graphene]}
    """

    pass


schema = build_schema(query=Query)
