from flask_classful import FlaskView, route


class User(FlaskView):
    route_base = "/"

    def get(self):
        return "this is from user"

    def post(self):
        return "this is a post request sent to User class view."


    @route('register')
    def user_registration(self):
        return "there will be a form that user can register him/her self."

