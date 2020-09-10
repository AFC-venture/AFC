from app import app
from flask import render_template, request,url_for

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about_afc')
def about_afc():
	return render_template('about.html')