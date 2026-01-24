from flask import Flask
from flask_cors import CORS
from database import db,migrate
from config import LocalDevelopmentConfig
from flask_security import Security, hash_password
from flask_restful import Api



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

def setup_database(app):
   #Create all tables
   db.create_all()
   

   


app=create_app()
if __name__=='__main__':
   app.run(debug=True)

