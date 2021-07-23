from flask_classful import FlaskView, route

from applications.graph.model import GraphModel


class GraphView(FlaskView):
    route_base = "/"

    def get(self):
        return "this is Graph"

    @route('create_graph')
    def create_graph(self):
        graph_model = GraphModel()
        graph_model.create_graph()
        return "graph created"
