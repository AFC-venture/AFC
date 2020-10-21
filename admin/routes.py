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
	unwanted_fields=['_sa_instance_state','updated_on','created_on']
	exec("global section_content;section_content="+section+".query.all()")
	print(section_content)
	return render_template("admin/edit.html", title="Edit",section=section,section_content=section_content,unwanted_fields=unwanted_fields)
