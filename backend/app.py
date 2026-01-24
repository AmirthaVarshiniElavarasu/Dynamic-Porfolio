from flask import Flask
from flask_cors import CORS
from database import db,migrate
from config import LocalDevelopmentConfig
from flask_security import Security, hash_password
from flask_restful import Api
from models import Admin
from dotenv import load_dotenv
import os



def create_app():
   app = Flask(__name__)
   # app config
   app.config.from_object(LocalDevelopmentConfig)
   # database setup
   db.init_app(app)
   migrate.init_app(app)

   CORS(app,supports_credentials=True)

   with app.app_context():
      setup_database(app)
   app.app_context().push()
   return app

def setup_database(app):
   #Create all tables
   db.create_all()
   if not Admin.query.first():
      email=os.getenv("ADMIN_EMAIL")
      password=os.getenv("ADMIN_PASSWORD")
      
      if not email or not password:
         raise RuntimeError("EMAIL OR PASSWORD NOT SET")

   admin=Admin(email=email,password_hash=hash_password(password))
   db.session.add(admin)
   db.session.commit()


app=create_app()
api=Api(app)

if __name__=='__main__':
   app.run(debug=True)

