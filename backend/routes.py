import resource
from flask import jsonify,request,make_response,send_from_directory
from flask_security import auth_required,current_user,utils
from .models import *
from flask_restful import Resource,reqparse

achievements= reqparse.RequestParser()
achievements.add_argument('description',type=str,required=True,help='description required')

class admin_login(resource):
    def post(self):
        login_credentials=request.get_json()

        if 'email' not in login_credentials or 'password' not in login_credentials:
            return make_response(jsonify({'message': 'email and password are required'}),400)
        
        email=login_credentials.get('email')
        password=login_credentials.get('password')

        user=db.first_or_404(email=email)
        if not user:
            return make_response(jsonify({"message": "User does not exist"}),404)
        if not utils.verify_password(password,user.password):
            return make_response(jsonify({"message":"User does not exist"}),404)
        utils.login_user(user)
        auth_token=user.get_auth_token()

        return{
            'message':'Login Sucessfully',
            'user':'admin'
        }        

class logout(resource):
    @auth_required('token')
    def post(self):
        utils.logout_user()
        return{'message':'Logout Successful'},200
class achievements(resource):
    @auth_required('token')
    def post(self):
        args=achievements.parse_args()
        new_description=Achievements(new_description=args['description'])
        db.session.add(new_description)
        db.session.commit()
        return {'message':'new achievement added successful'}

