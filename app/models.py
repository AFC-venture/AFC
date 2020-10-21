from app import app,db 
from sqlalchemy import func,text
from sqlalchemy.orm import backref
from datetime import datetime
from sqlalchemy.dialects.mysql import LONGTEXT

class AfcPages(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	page = db.Column( db.String(255), nullable=True )
	sections = db.Column( LONGTEXT, nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.page

# Home page
class HomeBanner(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	title = db.Column( db.String(255), nullable=True )
	image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.title

class HomeAboutUsSection(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	content = db.Column( LONGTEXT, nullable=True )
	icons = db.relationship( 'HomeAboutUsSectionIcons',backref="section_obj",lazy="dynamic" )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.title

class HomeAboutUsSectionIcons(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	section =  db.Column( db.Integer, db.ForeignKey('home_about_us_section.id')) 
	description = db.Column( db.String(255), nullable=True )
	static_image = db.Column( db.String(255), nullable=True )
	hover_image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.description

class RecentProjects(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	description = db.Column( db.String(255), nullable=True )
	image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.description

class Testimonial(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	testimonial = db.Column( LONGTEXT, nullable=True )
	client_name = db.Column( db.String(255), nullable=True )
	client_logo = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.client_name

class OurClients(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	client_logo = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.client_name

class CertificationCompliance(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.certification_name
# End

# About Us page
class AboutUsBanner(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	title = db.Column( db.String(255), nullable=True )
	image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.title

class AboutUsSection(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	heading = db.Column( db.String(255), nullable=True )
	content = db.Column( db.String(255), nullable=True )
	icons = db.relationship( 'AboutUsSectionIcons',backref="section_obj",lazy="dynamic" )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.title

class AboutUsSectionIcons(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	section =  db.Column( db.Integer, db.ForeignKey('about_us_section.id')) 
	description = db.Column( db.String(255), nullable=True )
	static_image = db.Column( db.String(255), nullable=True )
	hover_image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.description

class MissionVision(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	heading = db.Column( db.String(255), nullable=True )
	content = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.heading


class OurTeam(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	heading = db.Column( db.String(255), nullable=True )
	name = db.Column( db.String(255), nullable=True )
	designation = db.Column( db.String(255), nullable=True )
	image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.heading

class Infrastructure(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	image = db.Column( db.String(255), nullable=True )
	name = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.name
# End

# Products Page
class ProductCategory(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	sub_category = db.relationship( 'ProductSubCategory',backref="category_obj",lazy="dynamic" )
	image = db.Column( db.String(255), nullable=True )
	name = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.name

class ProductSubCategory(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	category =  db.Column( db.Integer, db.ForeignKey('product_category.id')) 
	name = db.Column( db.String(255), nullable=True )
	item = db.relationship( 'ProductSubCategoryItems',backref="sub_category_obj",lazy="dynamic" )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.name

class ProductSubCategoryItems(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	sub_category =  db.Column( db.Integer, db.ForeignKey('product_sub_category.id')) 
	name = db.Column( db.String(255), nullable=True )
	image = db.Column( db.String(255), nullable=True )
	description = db.Column( LONGTEXT , nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.name
# End

# Projects Page
class Projects(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	heading = db.Column( db.String(255), nullable=True )
	description = db.Column( db.String(255), nullable=True )
	image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.description
# End

# Clients Page
class AboutClients(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	heading = db.Column( db.String(255), nullable=True )
	content = db.Column( db.String(255), nullable=True )
	categories = db.relationship( 'AboutClientsCategories',backref="section_obj",lazy="dynamic" )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.title

class AboutClientsCategories(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	section =  db.Column( db.Integer, db.ForeignKey('about_clients.id')) 
	description = db.Column( db.String(255), nullable=True )
	static_image = db.Column( db.String(255), nullable=True )
	hover_image = db.Column( db.String(255), nullable=True )
	clients = db.relationship( 'CategoryClients',backref="category_obj",lazy="dynamic" )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.description

class CategoryClients(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	category =  db.Column( db.Integer, db.ForeignKey('about_clients_categories.id')) 
	image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.image
# End

# Latest at AFC Page
class LatestBanner(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	title = db.Column( db.String(255), nullable=True )
	image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.title

class WhatsNewSection(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	heading = db.Column( db.String(255), nullable=True )
	content = db.Column( db.String(255), nullable=True )
	image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.content

class FridaysAtAfc(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	heading = db.Column( db.String(255), nullable=True )
	content = db.Column( db.String(255), nullable=True )
	images = db.relationship( 'FridaysAtAfcImages',backref="section_obj",lazy="dynamic" )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.heading

class FridaysAtAfcImages(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	section = db.Column( db.Integer, db.ForeignKey('fridays_at_afc.id')) 
	location = db.Column( db.String(255), nullable=True )
	image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.description

class SocialMedia(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	heading = db.Column( db.String(255), nullable=True )
	title = db.Column( db.String(255), nullable=True )
	image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.title
# End

# Contact Us Page
class ContactUsBanner(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	title = db.Column( db.String(255), nullable=True )
	image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.title

class ContactForm(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	heading = db.Column( db.String(255), nullable=True )
	sub_heading = db.Column( db.String(255), nullable=True )
	form_fields = db.relationship( 'ContactFormFields',backref="form_obj",lazy="dynamic" )
	image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.heading

class ContactFormFields(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	form =  db.Column( db.Integer, db.ForeignKey('contact_form.id')) 
	name = db.Column( db.String(255), nullable=True )
	type = db.Column( db.String(255), nullable=True )
	placeholder = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.name

class ExperienceAfc(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	heading = db.Column( db.String(255), nullable=True )
	type = db.Column( db.String(255), nullable=True )
	locations = db.relationship( 'ContactInfo',backref="section_obj",lazy="dynamic" )
	image =  db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.heading

class ContactInfo(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	section = db.Column( db.Integer, db.ForeignKey('experience_afc.id')) 
	location = db.Column( db.String(255), nullable=True )
	address =  db.Column( db.String(255), nullable=True )
	landline =  db.Column( db.String(255), nullable=True )
	mobile =  db.Column( db.String(255), nullable=True )
	email = db.Column( db.String(255), nullable=True )
	latitude = db.Column( db.String(255), nullable=True )
	logitude = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.location
# End 	