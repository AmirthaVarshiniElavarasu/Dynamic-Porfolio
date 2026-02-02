from flask import Flask
from flask_cors import CORS
from database import db,migrate
from config import LocalDevelopmentConfig
from flask_security import Security, hash_password
from werkzeug.security import generate_password_hash
from flask_restful import Api
from models import Admin
from dotenv import load_dotenv
from routes import *
import os

load_dotenv()

def setup_database(app):
   with app.app_context():
      #Create all tables
      db.create_all()
      if not Admin.query.first():
         email=os.getenv("ADMIN_EMAIL")
         password=os.getenv("ADMIN_PASSWORD")
         
         if not email or not password:
            raise RuntimeError("EMAIL OR PASSWORD NOT SET")

         admin=Admin(email=email,password_hash=generate_password_hash(password))
         db.session.add(admin)
         db.session.commit()

def create_app():
   app = Flask(__name__)
   # app config
   app.config.from_object(LocalDevelopmentConfig)
   # database setup
   db.init_app(app)
   migrate.init_app(app,db)
   CORS(app,supports_credentials=True)

   setup_database(app)
   
   return app


app=create_app()
api=Api(app)
register_routes(api)

if __name__=='__main__':
   app.run(debug=True)
