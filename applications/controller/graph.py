from flask_classful import FlaskView


class Graph(FlaskView):

    route_base = "/"

    def get(self):
        return "this is Graph"
