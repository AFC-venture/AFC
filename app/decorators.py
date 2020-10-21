from flask_login import current_user
from flask import redirect,flash,url_for
from admin.models import Admin


def Admin_check(function):

	def check_admin(*args,**kwargs):
		endpoint = current_user.get_id().split("|")[1]
		if endpoint=="admin":
			return function(*args,**kwargs)
		else:
			flash('Permission Denied','danger')
			return redirect( url_for( 'admin.admin_login' ) )
	return check_admin
