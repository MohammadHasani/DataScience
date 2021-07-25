from flask import render_template, request
from flask_classful import FlaskView
from markupsafe import Markup

from applications.graph.model import GraphModel


class GraphView(FlaskView):
    route_base = "/"

    def get(self):
        file_name = request.args.get('file_name')
        graph_model = GraphModel()
        graph_html = Markup(graph_model.create_graph(file_name=file_name))
        return render_template("/graph/graph.html", data={"graph_html": graph_html})

    # @route('create_graph')
    # def create_graph(self):
    #
    #     return "graph created"
