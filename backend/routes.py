from flask import request
from flask_restful import Resource, reqparse
from werkzeug.security import check_password_hash
from flask import session
from datetime import datetime
from functools import wraps


from database import db
from models import (
    Admin, Achievements, SkillCategory, Skill,
    ProjectName, ProjectDescription,
    Work, WorkDescription,
    CareerObject, AboutMe, Education
)

# ---------- PARSERS ---------- #

def text_parser(required=True):
    p = reqparse.RequestParser()
    p.add_argument("text", type=str, required=required)
    return p


achievement_parser = reqparse.RequestParser()
achievement_parser.add_argument("description", type=str, required=True)

skill_category_parser = reqparse.RequestParser()
skill_category_parser.add_argument("title", type=str, required=True)

skill_parser = reqparse.RequestParser()
skill_parser.add_argument("name", type=str, required=True)
skill_parser.add_argument("category_id", type=int, required=True)

project_parser = reqparse.RequestParser()
project_parser.add_argument("title", type=str, required=True)
project_parser.add_argument("github_link", type=str, required=True)
project_parser.add_argument("hosted_link", type=str)
project_parser.add_argument("notes", type=str)

education_parser = reqparse.RequestParser()
education_parser.add_argument("join_date", type=str, required=True)
education_parser.add_argument("completion_date", type=str)
education_parser.add_argument("course_name", type=str)
education_parser.add_argument("course_work", type=str)
education_parser.add_argument("CGPA", type=float)
education_parser.add_argument("CGPA_outof", type=float)
education_parser.add_argument("order", type=int)

# ---------- AUTH ---------- #

class AdminLogin(Resource):
    def post(self):
        data = request.get_json()
        user = Admin.query.filter_by(email=data.get("email")).first()

        if not user or not check_password_hash(
            user.password_hash,data.get("password")
        ):
            return {"message": "Invalid credentials"}, 401

        session["admin_id"]=user.id
        return {"message": "Login success"}, 200


class Logout(Resource):
    def post(self):
        session.pop("admin_id",None)
        return {"message": "Logged out"}, 200

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        if "admin_id" not in session:
            return {"message": "Unauthoried"},401
        return fn(*args,**kwargs)
    return wrapper
# ---------- GENERIC CRUD MIXIN ---------- #

class CRUDBase(Resource):
    model = None
    parser = None
    protected = True
    method_decorators = [admin_required]

    def get(self, id=None):
        if id:
            obj = self.model.query.get_or_404(id)
            return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

        return [
            {c.name: getattr(o, c.name) for c in o.__table__.columns}
            for o in self.model.query.all()
        ]

    def post(self):
        args = self.parser.parse_args()
        obj = self.model(**args)
        db.session.add(obj)
        db.session.commit()
        return {"message": "Created"}, 201

    def put(self, id):
        obj = self.model.query.get_or_404(id)
        args = self.parser.parse_args()
        for k, v in args.items():
            setattr(obj, k, v)
        db.session.commit()
        return {"message": "Updated"}

    def delete(self, id):
        obj = self.model.query.get_or_404(id)
        db.session.delete(obj)
        db.session.commit()
        return {"message": "Deleted"}


# ---------- ACHIEVEMENTS ---------- #

class AchievementsAPI(CRUDBase):
    model = Achievements
    parser = achievement_parser


# ---------- SKILL CATEGORY ---------- #

class SkillCategoryAPI(CRUDBase):
    model = SkillCategory
    parser = skill_category_parser


# ---------- SKILLS ---------- #

class SkillsAPI(CRUDBase):
    model = Skill
    parser = skill_parser


# ---------- PROJECTS ---------- #

class ProjectAPI(CRUDBase):
    model = ProjectName
    parser = project_parser


class ProjectDescriptionAPI(CRUDBase):
    model = ProjectDescription
    parser = text_parser()


# ---------- WORK ---------- #

class WorkAPI(CRUDBase):
    model = Work
    parser = reqparse.RequestParser() \
        .add_argument("position", type=str, required=True) \
        .add_argument("company", type=str, required=True) \
        .add_argument("join_date", type=str, required=True) \
        .add_argument("resignation_date", type=str) \
        .add_argument("place", type=str, required=True) \
        .add_argument("order", type=int)
    def post(self):
        args=self.parser.parse_args()

        # convert string -> date
        args["join_date"]= datetime.strptime(args["join_date"], "%Y-%m-%d").date()

        if args.get("resignation_date"):
            args["resignation_date"]=datetime.strptime(args["resignation_date"],"%Y-%m-%d").date()
        obj=Work(**args)
        db.session.add(obj)
        db.session.commit()
        return {"message":"Created"},201


class WorkDescriptionAPI(CRUDBase):
    model = WorkDescription
    parser = text_parser()


# ---------- CAREER OBJECT ---------- #

class CareerObjectAPI(CRUDBase):
    model = CareerObject
    parser = reqparse.RequestParser() \
        .add_argument("title", type=str) \
        .add_argument("text", type=str)


# ---------- ABOUT ME ---------- #

class AboutMeAPI(CRUDBase):
    model = AboutMe
    parser = text_parser()


# ---------- EDUCATION ---------- #

class EducationAPI(CRUDBase):
    model = Education
    parser = education_parser

    def post(self):
        args=self.parser.parse_args()

        args["join_date"] = datetime.strptime(args["join_date"],"%Y-%m-%d").date()

        if args.get("completion_date"):
            args["completion_date"]= datetime.strptime(args["completion_date"],"%Y=%m%d").date()
        obj=self.model(**args)
        db.session.add(obj)
        db.session.commit()

        return {"message":"Created"},201


def register_routes(api):
    api.add_resource(AdminLogin,"/api/AdminLogin")
    api.add_resource(Logout,"/api/Logout")
    api.add_resource(AchievementsAPI, "/api/achievements", "/api/achievements/<int:id>")
    api.add_resource(SkillCategoryAPI, "/api/skill-categories", "/api/skill-categories/<int:id>")
    api.add_resource(SkillsAPI, "/api/skills", "/api/skills/<int:id>")
    api.add_resource(ProjectAPI, "/api/projects", "/api/projects/<int:id>")
    api.add_resource(ProjectDescriptionAPI, "/api/project-descriptions", "/api/project-descriptions/<int:id>")
    api.add_resource(WorkAPI, "/api/work", "/api/work/<int:id>")
    api.add_resource(WorkDescriptionAPI, "/api/work-descriptions", "/api/work-descriptions/<int:id>")
    api.add_resource(CareerObjectAPI, "/api/career-object", "/api/career-object/<int:id>")
    api.add_resource(AboutMeAPI, "/api/about-me", "/api/about-me/<int:id>")
    api.add_resource(EducationAPI, "/api/education", "/api/education/<int:id>")
