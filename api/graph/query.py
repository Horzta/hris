from graphene import ObjectType, String, Schema

class Query(ObjectType):
    hello = String()
    goodbye = String()

    def resolve_hello(self, info):
        return "Hello World"



    def resolve_goodbye(self, info):
        return "Bye bye!"
