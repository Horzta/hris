from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from database.objects import User


class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node,)
