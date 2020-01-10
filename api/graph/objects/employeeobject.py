from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from database.objects import Employee


class EmployeeObject(SQLAlchemyObjectType):
    class Meta:
        model = Employee
        interfaces = (relay.Node,)
