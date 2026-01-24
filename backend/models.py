from .database import db


class Admin(db.Model):
    __tablename__="Admin"
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(150),nullable=False,unique=True)
    password_hash =db.Column(db.String(255),nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

class Achievements(db.Model):
    __tablename__="Achievements"
    id=db.Column(db.Integer,primary_key=True)
    description=db.Column(db.String(500),nullable=False)

class SkillCategory(db.Model):
    __tablename__="Skill_Category"
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    order = db.Column(db.Integer, default=0)
    skills=db.relationship("Skill",backref="category", cascade="all, delete",lazy="select")

class Skill(db.Model):
    __tablename__="Skill"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    category_id=db.Column(db.Integer,db.ForeignKey("Skill_Category.id"),nullable=False)
    
class ProjectName(db.Model):
    __tablename__="Project_Name"
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    github_link=db.Column(db.String(500),nullable=False)
    hosted_link=db.Column(db.String(500),nullable=True)
    notes=db.Column(db.String(500))
    order = db.Column(db.Integer, default=0)

    project_description=db.relationship("Project_Description",backref="project",cascade="all, delete",lazy="select")

class ProjectDescription(db.Model):
    __tablename__="Project_Description"
    id=db.Column(db.Integer,primary_key=True)
    text=db.Column(db.Text)
    project_id=db.Column(db.Integer,db.ForeignKey("Project_Name.id"),nullable=False)

class Work(db.Model):
    __tablename__="Work"
    id=db.Column(db.Integer,primary_key=True)
    position=db.Column(db.String(500),nullable=False)
    company=db.Column(db.String(200),nullable=False)
    join_date=db.Column(db.date,nullable=False)
    resignation_date=db.Column(db.date,nullable=True)
    place=db.Column(db.String(200),nullable=False)
    order = db.Column(db.Integer, default=0)
    work_description=db.relationship("WorkDescription", backref="work", cascade="all, delete",lazy="select")

class WorkDescription(db.Model):
    __tablename__="Work_Description"
    id=db.Column(db.Integer, primary_key=True)
    text=db.Column(db.Text)
    work_id=db.Column(db.Integer,db.ForeignKey("Work.id"),nullable=False)

class CareerObject(db.Model):
    __tablename__="Career_Object"
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(300))
    text=db.Column(db.Text)

class AboutMe(db.Model):
    __tablename__="About_Me"
    id=db.Column(db.Integer,primary_key=True)
    text=db.Column(db.Text)

class Education(db.Model):
    __tablename__="Education"
    id=db.Column(db.Integer,primary_key=True)
    join_date=db.Column(db.date,nullable=False)
    completion_date=db.Column(db.date,nullable=True)
    course_name=db.Column(db.String(300))
    course_work=db.Column(db.Text)
    CGPA=db.Column(db.Float)
    CGPA_outof=db.Column(db.Float)
    order = db.Column(db.Integer, default=0)
