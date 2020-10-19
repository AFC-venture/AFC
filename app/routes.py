from app import app,db
from app.models import *
from flask import render_template, request, url_for, jsonify


@app.route("/get_products_data",methods=['GET'])
def get_products_data():
	categories=ProductCategory.query.all()
	cates=[]
	for category in categories:
		cate={}
		cate['cat_name']=category.name
		cate['sub_cates']=[]
		for sub_category in category.sub_category.all():
			sub_cate={}
			sub_cate['name']=sub_category.name
			sub_cate['link']=url_for('products_sub_category',sub_category=sub_category.name)
			cate['sub_cates'].append(sub_cate)
		cates.append(cate)
	return jsonify({'categories':cates})

@app.route('/')
def home():		
	return render_template('home.html')

@app.route('/about_afc')
def about_afc():
	return render_template('about.html')

@app.route('/products')
def products():
	return render_template('products.html')

@app.route('/desk_based_desc')
def desk_based_desc():
	return render_template('desk_based_desc.html')

@app.route('/products/<string:sub_category>')
def products_sub_category(sub_category):
	sub_category=ProductSubCategory.query.filter_by(name=sub_category).first()
	if sub_category.item.first().name==sub_category.name:
		cat_type=2
		sub_category=sub_category.category_obj
	else:
		cat_type=1
	return render_template('products_sub_category.html',type=cat_type,sub_category=sub_category)

@app.route('/products/<string:sub_category>/details')
def products_sub_category_details(sub_category):
	sel_item=ProductSubCategoryItems.query.filter_by(name=request.args['item']).first()
	try:
		sub_cat=ProductSubCategory.query.filter_by(name=sub_category).first()
		l_items=sub_cat.item.all()
	except:
		sub_cat=ProductCategory.query.filter_by(name=sub_category).first()
		l_items=[]
		for cat in sub_cat.sub_category.all():
			l_items.append(cat.item.first())
	l_items.remove(sel_item)
	items=[sel_item]+l_items
	items=list(enumerate(items))
	print(sel_item,items)
	return render_template('products_sub_category_details.html',items=items,length=len(items))

@app.route('/projects')
def projects():
	return render_template('projects.html')

@app.route('/projects_gallery')
def projects_gallery():
	return render_template('projects_gallery.html')

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

