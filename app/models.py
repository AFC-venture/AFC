from app import app,db 
from sqlalchemy import func,text
from sqlalchemy.orm import backref
from datetime import datetime
from sqlalchemy.dialects.mysql import LONGTEXT

class AfcPages(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	priority = db.Column( db.Integer, nullable=True )
	page = db.Column( db.String(255), nullable=True )
	sections = db.Column( LONGTEXT, nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.page

	def is_foreign_key(column):
		if column.foreign_keys :
			return True 
		else:
			return False

# Home page
class HomeBanner(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	title = db.Column( db.String(255), nullable=True )
	image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.title

	def is_foreign_key(column):
		if column.foreign_keys :
			return True 
		else:
			return False

class HomeAboutUsSection(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	content = db.Column( LONGTEXT, nullable=True )
	icons = db.relationship( 'HomeAboutUsSectionIcons',backref="parent_obj",lazy="dynamic" )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return "{} - {}".format(self.id,self.content)

	def is_foreign_key(column):
		if column.foreign_keys :
			return True 
		else:
			return False

class HomeAboutUsSectionIcons(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	section =  db.Column( db.Integer, db.ForeignKey('home_about_us_section.id')) 
	description = db.Column( db.String(255), nullable=True )
	static_image = db.Column( db.String(255), nullable=True )
	hover_image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return "{} - {}".format(self.id,self.description)

	def is_foreign_key(column):
		if column.foreign_keys :
			return True 
		else:
			return False

class RecentProjects(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	description = db.Column( db.String(255), nullable=True )
	image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.description

	def is_foreign_key(column):
		if column.foreign_keys :
			return True 
		else:
			return False

class Testimonial(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	testimonial = db.Column( LONGTEXT, nullable=True )
	client_name = db.Column( db.String(255), nullable=True )
	client_logo = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.client_name

	def is_foreign_key(column):
		if column.foreign_keys :
			return True 
		else:
			return False

class OurClients(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	client_logo = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.client_name

	def is_foreign_key(column):
		if column.foreign_keys :
			return True 
		else:
			return False

class CertificationCompliance(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.certification_name

	def is_foreign_key(column):
		if column.foreign_keys :
			return True 
		else:
			return False
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

	def is_foreign_key(column):
		if column.foreign_keys :
			return True 
		else:
			return False

class AboutUsSection(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	heading = db.Column( db.String(255), nullable=True )
	content = db.Column( db.String(255), nullable=True )
	icons = db.relationship( 'AboutUsSectionIcons',backref="parent_obj",lazy="dynamic" )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return "{} - {}".format(self.id,self.title)

	def is_foreign_key(column):
		if column.foreign_keys :
			return True 
		else:
			return False

class AboutUsSectionIcons(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	section =  db.Column( db.Integer, db.ForeignKey('about_us_section.id')) 
	description = db.Column( db.String(255), nullable=True )
	static_image = db.Column( db.String(255), nullable=True )
	hover_image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return "{} - {}".format(self.id,self.description)

	def is_foreign_key(column):
		if column.foreign_keys :
			return True 
		else:
			return False

class MissionVision(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	heading = db.Column( db.String(255), nullable=True )
	content = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.heading

	def is_foreign_key(column):
		if column.foreign_keys :
			return True 
		else:
			return False


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

	def is_foreign_key(column):
		if column.foreign_keys :
			return True 
		else:
			return False

class Infrastructure(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	image = db.Column( db.String(255), nullable=True )
	name = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.name

	def is_foreign_key(column):
		if column.foreign_keys :
			return True 
		else:
			return False
# End

# Products Page
class ProductsBanner(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	title = db.Column( db.String(255), nullable=True )
	image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.title

	def is_foreign_key(column):
		if column.foreign_keys :
			return True 
		else:
			return False

class ProductsPromiseSection(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	content = db.Column( LONGTEXT, nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.title

	def is_foreign_key(column):
		if column.foreign_keys :
			return True 
		else:
			return False

class ProductCategory(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	sub_category = db.relationship( 'ProductSubCategory',backref="parent_obj",lazy="dynamic" )
	image = db.Column( db.String(255), nullable=True )
	name = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return "{} - {}".format(self.id,self.name)

	def is_foreign_key(column):
		if column.foreign_keys :
			return True 
		else:
			return False

class ProductSubCategory(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	category =  db.Column( db.Integer, db.ForeignKey('product_category.id')) 
	name = db.Column( db.String(255), nullable=True )
	item = db.relationship( 'ProductSubCategoryItems',backref="parent_obj",lazy="dynamic" )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return "{} - {}".format(self.id,self.name)

	def is_foreign_key(column):
		if column.foreign_keys :
			return True 
		else:
			return False

class ProductSubCategoryItems(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	sub_category =  db.Column( db.Integer, db.ForeignKey('product_sub_category.id')) 
	name = db.Column( db.String(255), nullable=True )
	image = db.Column( db.String(255), nullable=True )
	description = db.Column( LONGTEXT , nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return "{} - {}".format(self.id,self.name)

	def is_foreign_key(column):
		if column.foreign_keys :
			return True 
		else:
			return False
# End

# Projects Page
class ProjectsBanner(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	name = db.Column( db.String(255), nullable=True )
	image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.name

class ProjectsGallery(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	heading = db.Column( db.String(255), nullable=True )
	description = db.Column( db.String(255), nullable=True )
	image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.description

class AllProjects(db.Model):
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
class ClientsBanner(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	name = db.Column( db.String(255), nullable=True )
	image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return self.name

class AboutClients(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	heading = db.Column( db.String(255), nullable=True )
	content = db.Column( db.String(255), nullable=True )
	categories = db.relationship( 'AboutClientsCategories',backref="parent_obj",lazy="dynamic" )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return "{} - {}".format(self.id,self.title)

class AboutClientsCategories(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	section =  db.Column( db.Integer, db.ForeignKey('about_clients.id')) 
	description = db.Column( db.String(255), nullable=True )
	static_image = db.Column( db.String(255), nullable=True )
	hover_image = db.Column( db.String(255), nullable=True )
	clients = db.relationship( 'CategoryClients',backref="parent_obj",lazy="dynamic" )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return "{} - {}".format(self.id,self.description)

class CategoryClients(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	category =  db.Column( db.Integer, db.ForeignKey('about_clients_categories.id')) 
	image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return "{} - {}".format(self.id,self.image)
# End

# Latest at AFC Page
class LatestBanner(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	title = db.Column( db.String(255), nullable=True )
	image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return "{} - {}".format(self.id,self.title)

class WhatsNewSection(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	heading = db.Column( db.String(255), nullable=True )
	content = db.Column( db.String(255), nullable=True )
	image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return "{} - {}".format(self.id,self.content)

class FridaysAtAfc(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	heading = db.Column( db.String(255), nullable=True )
	content = db.Column( db.String(255), nullable=True )
	images = db.relationship( 'FridaysAtAfcImages',backref="parent_obj",lazy="dynamic" )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return "{} - {}".format(self.id,self.heading)

class FridaysAtAfcImages(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	section = db.Column( db.Integer, db.ForeignKey('fridays_at_afc.id')) 
	image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return "{} - {}".format(self.id,self.description)

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
	form_fields = db.relationship( 'ContactFormFields',backref="parent_obj",lazy="dynamic" )
	image = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return "{} - {}".format(self.id,self.heading)

class ContactFormFields(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	form =  db.Column( db.Integer, db.ForeignKey('contact_form.id')) 
	name = db.Column( db.String(255), nullable=True )
	type = db.Column( db.String(255), nullable=True )
	placeholder = db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return "{} - {}".format(self.id,self.name)

class ExperienceAfc(db.Model):
	id = db.Column( db.Integer, primary_key=True )
	heading = db.Column( db.String(255), nullable=True )
	type = db.Column( db.String(255), nullable=True )
	locations = db.relationship( 'ContactInfo',backref="parent_obj",lazy="dynamic" )
	image =  db.Column( db.String(255), nullable=True )
	created_on = db.Column( db.DateTime, default=datetime.now )
	updated_on = db.Column( db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP') )

	def __repr__(self):
		return "{} - {}".format(self.id,self.heading)

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
		return "{} - {}".format(self.id,self.location)
# End 	