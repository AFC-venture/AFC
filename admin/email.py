from flask_mail import Message
from flask import render_template, request, url_for
from app import app
from app import mail
from threading import Thread
import os


def send_email(subject, text_body, html_body,attachment=None):
	msg = Message(subject, sender=app.config['ADMINS'][0], recipients=['engg@turningideas.com'])
	msg.body=text_body
	msg.html=html_body
	if attachment:
		ext=os.path.splitext(attachment.filename)
		msg.attach(attachment.filename,'application/'+ext[1],attachment.read())
	Thread( target=send_async_email, args=(app, msg) ).start()
	

def send_async_email(app,msg):
	with app.app_context():
		mail.send(msg)

def send_reset_password_email(admin, token):
	reset_password_link = "http://"+ request.host + url_for('admin.admin_reset_password', token=token)
	msg = Message("[Reset Password]", sender=app.config['ADMINS'][0], recipients=[admin.email])
	msg.body=None
	msg.html=render_template("admin/email/reset_password.html", admin=admin, token=token, reset_password_link=reset_password_link)
	Thread( target=send_async_email, args=(app, msg) ).start()

def send_volunteer_rq_approve_email(volunteer, password):
	msg = Message("[Volunteer Request Approved]", sender=app.config['ADMINS'][0], recipients=[volunteer.email])
	msg.body=None
	msg.html=render_template("admin/email/volunteer_rq_approve_email.html", volunteer=volunteer, password=password)
	Thread( target=send_async_email, args=(app, msg) ).start()

def send_volunteer_rq_reject_email(volunteer):
	msg = Message("[Volunteer Request Reject]", sender=app.config['ADMINS'][0], recipients=[volunteer.email])
	msg.body=None
	msg.html=render_template("admin/email/volunteer_rq_reject_email.html", volunteer=volunteer)
	Thread( target=send_async_email, args=(app, msg) ).start()