from graphene import ObjectType, List, relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from graph.objects.accountobject import AccountObject
from common.containers import Databases
from database.objects import Account

class Viewer(ObjectType):
    class Meta:
        interfaces = (relay.Node,)

    all_accounts = SQLAlchemyConnectionField(AccountObject)
