from app import app
from flask import render_template, request,url_for

@app.route('/')
def home():		
	return render_template('home.html')

@app.route('/about_afc')
def about_afc():
	return render_template('about.html')

@app.route('/projects')
def projects():
	return render_template('projects.html')

@app.route('/all_projects')
def all_projects():
	return render_template('all_projects.html')

@app.route('/clients')
def clients():
	return render_template('clients.html')

@app.route('/contact_us')
def contact_us():
	return render_template('contact_us.html', site_key=app.config["RECAPTCHA_SITE_KEY"])

@app.route('/latest')
def latest():
	return render_template('latest.html')