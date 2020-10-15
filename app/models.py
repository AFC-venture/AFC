from app import app,db 
from sqlalchemy import func,text
from sqlalchemy.orm import backref
from datetime import datetime
from sqlalchemy.dialects.mysql import LONGTEXT


class ProductCategory(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	name = db.Column( db.String(255), nullable=False )
	sub_category = db.relationship( 'ProductSubCategory',backref="category_obj",lazy="dynamic" )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.name

class ProductSubCategory(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	category =  db.Column( db.Integer, db.ForeignKey('product_category.id')) 
	name = db.Column( db.String(255), nullable=False )
	item = db.relationship( 'ProductSubCategoryItems',backref="sub_category_obj",lazy="dynamic" )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.name

class ProductSubCategoryItems(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	sub_category =  db.Column( db.Integer, db.ForeignKey('product_sub_category.id')) 
	name = db.Column( db.String(255), nullable=False )
	image = db.Column( db.String(255), nullable=False )
	description = db.Column( LONGTEXT , nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.name

