from flask_login import login_user, login_required, logout_user, current_user
from . import admin_app
from .models import Admin , db
from app.models import *
from app.decorators import Admin_check
from flask import redirect, render_template, flash, request, abort, url_for, jsonify, make_response
from datetime import datetime
import csv
import random
import io
import os
from PIL import Image as pil_img

def generate_password():
	MAX_LEN = 12
	DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
	LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
					 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
					 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
					 'z'] 
  
	UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
					 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 
					 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
					 'Z'] 
  
	SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
					'*', '(', ')', '<&# 039;'] 

	COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS 

	rand_digit = random.choice(DIGITS) 
	rand_upper = random.choice(UPCASE_CHARACTERS) 
	rand_lower = random.choice(LOCASE_CHARACTERS) 
	rand_symbol = random.choice(SYMBOLS) 
	temp_pass = list( rand_digit + rand_upper + rand_lower + rand_symbol ) 
	for x in range(MAX_LEN - 4): 
		temp_pass = temp_pass + [ random.choice(COMBINED_LIST) ]
		random.shuffle( list(temp_pass) )

	return "".join(temp_pass)


@admin_app.route("/login",methods=["GET","POST"])
def admin_login():
	if request.method=="GET" and current_user.is_authenticated:
		return redirect(url_for("admin.admin_dashboard"))
	if request.method=="POST":
		data = request.form.to_dict()
		if "email" in data and "password" in data:
			admin = Admin.query.filter_by( email=data["email"].strip() ).first()
			if admin and admin.check_password( data["password"] ):
				if login_user(admin, remember=("remember_me" in data)):
					flash("Welcome {}".format( admin.first_name ),"success")
					return redirect(url_for("admin.admin_dashboard"))
				else:
					abort(502)
			else:
				flash("Invalid Email or Password","danger")
				return redirect(url_for("admin.admin_login"))
	return render_template("admin/login.html", title="Admin Login")

@admin_app.route("/logout",methods=["GET","POST"], endpoint="admin_logout")
@login_required
@Admin_check
def admin_logout():
	logout_user()
	return redirect(url_for("admin.admin_login"))

@admin_app.route("/reset_password_request",methods=["GET","POST"])
def admin_reset_password_request():
	if request.method=="POST":
		data = request.form.to_dict()
		if "email" in data:
			admin = Admin.query.filter_by(email=data["email"]).first()
			if admin:
				token = admin.get_reset_password_token()
				flash("Reset password link has been successfully sent to your mail {}".format(data["email"]),"success")
				send_reset_password_email(admin,token)
				return redirect(url_for("admin.admin_login"))
			else:
				flash("Invalid Email Address","danger")
				redirect(url_for("admin.admin_reset_password_request"))
	return render_template("admin/reset_password_request.html")

@admin_app.route("/reset_password/<string:token>",methods=["GET","POST"])
def admin_reset_password(token):
	admin = Admin.verify_reset_password_token(token)
	if admin:
		if request.method=="POST":
			data = request.form.to_dict()
			if "password1" in data and "password2" in data:
				if data["password1"]==data["password2"]:
					if not admin.check_password(data["password1"]):
						admin.set_password(data["password1"])
						db.session.commit()
						flash("Your Password has been sicessfully changed","success")
						login_user(admin)
						return redirect(url_for("admin.admin_dashboard"))
					else:
						flash("New password can't be same as old passowrd",'danger')
						return redirect(url_for("admin.admin_reset_password",token=token))
				else:
					flash("New password does not match with confirm password",'danger')
					return redirect(url_for("admin.admin_reset_password",token=token))
			
			flash("Invalid Data","danger")
			return redirect(url_for("admin.admin_reset_password",token=token))

		return render_template("admin/reset_password.html", token=token)
	else:
		flash('Invalid/Expired Token','danger')
		return redirect(url_for("admin.admin_login"))

@admin_app.route("/dashboard", methods=["GET","POST"], endpoint="admin_dashboard")
@login_required
@Admin_check
def admin_dashboard():
	pages = AfcPages.query.all()
	return render_template("admin/dashboard.html", title="Dashboard",pages=pages)


@admin_app.route("/edit/<string:section>", methods=["GET","POST"], endpoint="edit")
@login_required
@Admin_check
def edit(section): 
	unwanted_fields=['_sa_instance_state','updated_on','created_on','id','parent_obj']
	exec("global section_content;section_content="+section.strip()+".query.all()")
	exec("global section_fields;section_fields=list("+section.strip()+".__table__.columns)")
	
	form_fields=[]
	foreign_keys=[]
	for c in section_fields:
		form_fields.append(c.name)
		exec("global is_key;is_key="+section.strip()+".is_foreign_key("+section.strip()+"."+c.name.strip()+")")
		if is_key:
			foreign_keys.append(c.name)
	parent_objects=[]
	if foreign_keys:
		exec("global f_keys;f_keys="+section.strip()+".__table__.columns."+foreign_keys[0])
		for f_key in f_keys.__dict__["foreign_keys"]:
			parent=f_key._colspec.split('.')[0].split('_')
		parent_table=''
		for i in parent:
			parent_table+=i[0].upper()+i[1:].lower()
		exec("global parent_objects;parent_objects="+parent_table.strip()+".query.all()")
		print(parent_objects)
	sec_content=[]
	for content in section_content:
		c={}
		id=content.__dict__['id']
		exec("global fo_key;fo_key="+section.strip()+".query.filter_by(id="+str(id)+").first()")
		try:
			fo_key.parent_obj
		except:
			pass
		for field,value in content.__dict__.items():
			if field not in unwanted_fields:
				if field in foreign_keys:
					c[field]=content.__dict__['parent_obj']
				else:
					c[field]=value
		sec_content.append(c)

	return render_template("admin/edit.html", 
		title="Edit",
		section=section,
		sec_content=sec_content,
		unwanted_fields=unwanted_fields,
		form_fields=form_fields,
		foreign_keys=foreign_keys,
		parent_objects=parent_objects
		)

@admin_app.route("/delete_section", methods=["GET","POST"], endpoint="delete_section")
@login_required
@Admin_check
def delete_section():
	section=request.form["section"]
	content_id=request.form["id"]
	exec("global section_content;section_content="+section.strip()+".query.filter_by(id="+content_id.strip()+").first()")
	db.session.delete(section_content)
	db.session.commit()
	return jsonify({'reload':True})

def save_picture(form_picture):
	ext=os.path.splitext(form_picture.filename)
	picture_path=os.path.join(app.root_path+'/static/uploads/'+ext[0]+ext[1])
	# output_size = (125, 125)
	i = pil_img.open(form_picture)
	# i.thumbnail(output_size)
	i.save(picture_path)
	return 'uploads/'+ext[0]+ext[1]


@admin_app.route("/add_content", methods=["GET","POST"], endpoint="add_content")
@login_required
@Admin_check
def add_content():
	if request.method == "POST":
		print(request.form,request.files)
		section=request.form['page_section'].strip()
		object_attrs=''
		for key,value in request.form.items():
			if key!='page_section':
				exec("global is_key;is_key="+section.strip()+".is_foreign_key("+section.strip()+"."+key.strip()+")")
				if is_key:
					object_attrs+=key.strip()+" = '"+str(int(value.split('-')[0].strip()))+"',"
				else:
					object_attrs+=key.strip()+" = '"+value.strip()+"',"
		for key,value in request.files.items():
			object_attrs+=key+" = '"+save_picture(value).strip()+"',"
		print(object_attrs.strip(','))
		exec("global section_object;section_object="+section.strip()+"("+object_attrs+")")
		db.session.add(section_object)
		db.session.commit()
	return redirect(url_for('admin.edit',section=section))


def save_picture(form_picture):
	ext=os.path.splitext(form_picture.filename)
	picture_path=os.path.join(app.root_path+'/static/uploads/'+ext[0]+ext[1])
	# output_size = (125, 125)
	i = pil_img.open(form_picture)
	# i.thumbnail(output_size)
	i.save(picture_path)
	return 'uploads/'+ext[0]+ext[1]


@admin_app.route("/update_content", methods=["GET","POST"], endpoint="update_content")
@login_required
@Admin_check
def update_content():
	if request.method == "POST":
		section=request.form['page_section'].strip()
		org_object_attrs=''
		exec("global foreign_keys;foreign_keys="+section.strip()+".__table__.columns.sub_category")
		for foreign_key in foreign_keys.__dict__["foreign_keys"]:
			print(foreign_key._colspec.split('.'))
		new_attrs={}
		print(request.form)
		for key,value in request.form.items():
			if key!='page_section':
				if key.split('_')[0]=='org':
					exec("global is_key;is_key="+section.strip()+".is_foreign_key("+section.strip()+"."+'_'.join(key.split('_')[1:]).strip()+")")
					if not is_key:
						org_object_attrs+='_'.join(key.split('_')[1:]).strip()+" = '"+value.strip()+"',"
				elif value!=request.form['org_'+key]:
					exec("global is_key;is_key="+section.strip()+".is_foreign_key("+section.strip()+"."+key.strip()+")")
					if is_key:
						new_attrs[key]=int(value.split('-')[0].strip())
					else:
						new_attrs[key]=value
		exec("global section_object;section_object="+section.strip()+".query.filter_by("+org_object_attrs+").first()")
		for key,value in request.files.items():
			if value.filename!='':
				new_attrs[key]= save_picture(value).strip()
		print(new_attrs,section_object,is_key)
		for attr in new_attrs.items():
			exec("global is_key;is_key="+section.strip()+".is_foreign_key("+section.strip()+"."+attr[0].strip()+")")
			if is_key:
				exec("global section_object;section_object."+attr[0]+"='"+str(attr[1])+"'")
			else:
				exec("global section_object;section_object."+attr[0]+"='"+attr[1]+"'")
		db.session.commit()
	return redirect(url_for('admin.edit',section=section))

