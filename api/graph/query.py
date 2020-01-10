from graphene import ObjectType, Field, relay
from graph.viewer import Viewer

class Query(ObjectType):
    node = relay.Node.Field()
    viewer = Field(Viewer)

    @staticmethod
    def resolve_viewer(root, info):
        return Viewer()