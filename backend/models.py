from .database import db


class admin(db.Model):
    __tablename__="admin"
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(150),nullable=False,unique=True)
    password=db.Column(db.String(25),nullable=False)

class achivements(db.Model):
    __tablename__="achivement"
    id=db.Column(db.Integer,primary_key=True)
    description=db.Column(db.String(500))

class skillCategory(db.Model):
    __tablename__="skill_category"
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)

    skills=db.relationship("skill",backref="category", cascade="all, delete")

class skill(db.model):
    __tablename__="skill"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.string(100),nullable=False)
    category_id=db.Column(db.Integer,db.Foreignkey("skill_category.id"),nullable=False)
    
class project_name(db.model):
    __tablename__="project_name"
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    github_link=db.Column(db.String(500),nullable=False)
    hosted_link=db.Column(db.String(500,nullable=True))
    Notes=db.Column(db.String(500))
    project_description=db.relationship("project_description",backref="description",cascade="all, delete")

class project_description(db.model):
    __tablename__="project_description"
    id=db.Column(db.Integer,primary_key=True)
    text=db.Column(db.Text)
    