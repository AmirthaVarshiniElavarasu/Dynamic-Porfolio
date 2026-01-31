import resource
from flask import jsonify,request,make_response,send_from_directory
from flask_security import auth_required,current_user,utils
from .models import *
from flask_restful import Resource,reqparse

achievements= reqparse.RequestParser()
skill_category=reqparse.RequestParser()
skills=reqparse.RequestParser()
project=reqparse.RequestParser()
achievements.add_argument('description',type=str,required=True,help='description required')
skill_category.add_argument('title',type=str,required=True,help='title required')
skills.add_argument('name',type=str,required=True,help='skill name required')
skills.add_argument('category_id',type=int,required=True,help='Category id required')
project.add_argument('title',type=str,required=True,help='project name required')
project.add_argument('github_link',type=str,required=True,help='project repo link required')
project.add_argument('hosted_link',type=str,required=False,help='project hosted link not mandatory')
project.add_argument('notes',type=str,required=False,help='project notes not mandatory')

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
    def post(self):
        args=skills.prase_args()
        if Skill.query.filter_by(name=args['name']).first():
            return {'message': f'skill is already added'}
        new_skill=Skill(name=args['name'],category_id=args['category_id'])
        db.session.add(new_skill)
        db.session.commit()
        return {'message': 'New Skill added'}

    @auth_required
    def put(self,id):
        skill=Skill.query.get_or_404(id)
        args=skills.prase_args()

        skill.name=args['name']
        skill.category_id=args['category_id']
        
        return {'message': f'Skill changed to {args['name']}'}

    @auth_required
    def delete(self,id=None,cat_id=None):
        
        if id:
            skill=Skill.query.get_or_404(id)
            db.session.delete(skill)
            db.session.commit()
            return {'message':f'{skill.name} deleted successfully'}
        skill=Skill.query.get_or_404(cat_id)
        cat_title=SkillCategory.query.get_or_404(cat_id)
        db.session.delete(skill)
        db.session.commit()
        return {'message': f'All skills of the {cat_title} deleted Successfully'}
    
    @auth_required
    def get(self,id=None,cat_id=None):
        if id:
            skill=Skill.query.get_or_404(id)
            return skill.name
        skill=Skill.query.get_or_404(cat_id)
        return [s for s in skill]
class Projectname(resource):
    @auth_required
    def post(self):
        args=project.prase_args()
        if ProjectName.query.filter_by(title=args['title']).first():
            return {'message': f'{args['title']} is already added'}
        new_project=ProjectName(title=args['title'],github_link=args['github_link'],hosted_link=args['hosted_link'],notes=args['notes'])
        db.session.add(new_project)
        db.session.commit()
        return {'message':f'New project added successfully'}
    
    @auth_required
    def put(self,id):
        project_edit=ProjectName.query.get_or_404(id)
        args=project.prase_args()

        project_edit.title=args['title']
        project_edit.github_link=args['github_link']
        project_edit.hosted_link=args['hosted_link']
        project_edit.notes=args['notes']

        db.session.commit()
        return {'message': 'Project details changed successfully'}
    @auth_required
    def delete(self,id):
        