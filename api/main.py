from flask import Flask
from flask_graphql import GraphQLView
from graph.schema import schema

# app initialization
app = Flask(__name__)
app.debug = True

# Configs
# TO-DO

# Modules
# TO-DO

# Models
# TO-DO

# Schema Objects
# TO-DO

# Routes
# TO-DO
@app.route('/')
def index():
    return '<p> Hello World</p>'

# GraphQL Route
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))



if __name__ == '__main__':
     app.run()