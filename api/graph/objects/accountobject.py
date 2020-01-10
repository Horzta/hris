from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from database.objects import Account


class AccountObject(SQLAlchemyObjectType):
    class Meta:
        model = Account
        interfaces = (relay.Node,)
