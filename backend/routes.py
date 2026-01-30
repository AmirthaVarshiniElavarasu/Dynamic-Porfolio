import resource
from flask import jsonify,request,make_response,send_from_directory
from flask_security import auth_required,current_user,utils
from .models import *
from flask_restful import Resource,reqparse

achievements= reqparse.RequestParser()
skill_category=reqparse.RequestParser()
skills=reqparse.RequestParser()
achievements.add_argument('description',type=str,required=True,help='description required')
skill_category.add_argument('title',type=str,required=True,help='title required')
skills.add_argument('name',type=str,required=True,help='skill name required')
skills.add_argument('category_id',type=int,required=True,help='Category id required')

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
        new_description=Achievements(description=args['description'])
        db.session.add(new_description)
        db.session.commit()
        return {'message':'new achievement added successful'}
    @auth_required('token')
    def put(self,id):
        description=Achievements.query.get_or_404(id)
        args=achievements.parse_args()

        description.description=args['description']
        db.session.commit()

        return {'message': 'Achievements description updated successfully'}
    
    @auth_required('token')
    def delete(self,id):
        description=Achievements.query.get_or_404(id)

        db.session.delete(description)
        db.session.commit()
        return {'message':'Achievements description deleted successfully'}
    
    @auth_required('token')
    def get(self, id=None):
        if id:
            description=Achievements.query.get_or_404(id)
            return description
        description = Achievements.query.all()
        return description

class skill_category(resource):
    @auth_required('token')
    def post(self):
        args=skill_category.parse_args()
        if SkillCategory.query.filter_by(title=args['title']).first():
            return {'message': 'Skill category is already added'} 
        new_skill_cate=SkillCategory(title=args['title'])
        db.session.add(new_skill_cate)
        db.session.commit()
        return {'message': f'New Skill Category {new_skill_cate} added successfull'}
    @auth_required('token')
    def put(self,id):
        Skill_cate=SkillCategory.query.get_or_404(id)
        args=skill_category.parse_args()

        Skill_cate.title=args['title']
        db.session.commit()

        return {'message': f'Skill category changed to {Skill_cate.title}'}
    @auth_required('token')
    def delete(self,id):
        Skill_cate=SkillCategory.query.get_or_404(id)
        if Skill_cate.skills:
            return {'message':'Please delete the skills first'}
        
        db.session.delete(Skill_cate)
        db.session.commit()
        return{'message':f'Skill category {Skill_cate.title} deleted successfully'}
    @auth_required('token')
    def get(self,id=None):
        if id:
            Skill_cate=SkillCategory.query.get_or_404(id)
            return Skill_cate.title
        Skill_cate=SkillCategory.query.all()
        return [ s for s in Skill_cate]

class Skills(resource):
    @auth_required
    def post()