import resource
from flask import jsonify,request,make_response,send_from_directory
from flask_security import auth_required,current_user
from .models import *

class admin(resource):
    @auth_required('token')
    def get(self):
        


