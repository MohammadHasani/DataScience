from flask import render_template, current_app
from flask_classful import FlaskView, route


class User(FlaskView):
    route_base = "/"

    def get(self):
        return "this is from user"

    def post(self):
        return "this is a post request sent to User class view."

    @route('signup')
    def signup(self):
        return render_template('/user/signup.html')

