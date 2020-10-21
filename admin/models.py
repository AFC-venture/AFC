from app import app, db
from datetime import datetime
from time import time
from flask import url_for
import jwt
from time import time
import os
from sqlalchemy import func,text
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from time import time

class Admin(UserMixin, db.Model):
	id = db.Column( db.Integer, primary_key=True )
	first_name=db.Column( db.String(50), nullable=False )
	last_name=db.Column( db.String(50), nullable=True )
	email = db.Column( db.String(60), nullable=False, index=True )
	password_hash = db.Column( db.String(128), nullable=False )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def get_id(self):
		return "{}|{}".format(self.id,"admin")

	def get_reset_password_token(self,expire_in=360):
		return jwt.encode( {'reset_password':self.id, 'exp':time()+expire_in }, app.config['SECRET_KEY'], algorithm='HS256' ).decode('utf-8')

	@staticmethod
	def verify_reset_password_token(token):
		try:
			id = jwt.decode( token, app.config['SECRET_KEY'],algorithm=['HS256'] )['reset_password']
		except:
			return None
		return Admin.query.get(int(id))


	def set_password( self,password ):
		self.password_hash = generate_password_hash(password)

	def check_password( self,password ):
		return check_password_hash( self.password_hash, password ) 
