from flask import render_template
from flask_classful import FlaskView

from applications.graph.model import GraphModel


class GraphView(FlaskView):
    route_base = "/"

    def get(self):
        graph_model = GraphModel()
        graph_html = graph_model.create_graph()
        return render_template("/graph/graph.html", data={"graph_html": graph_html})

    # @route('create_graph')
    # def create_graph(self):
    #
    #     return "graph created"
