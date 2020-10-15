from app.models import *

desc='<p>\
 		Lorem ipsum dolor sit amet, consectetuer adipiscing\
		elit, sed diam nonummy nibh euismod tincidunt ut\
		laoreet dolore magna aliquam erat volutpat. Ut\
	</p>\
	<ul>\
		<li>Lorem ipsum dolor sit amet</li>\
		<li>Lorem ipsum dolor sit amet</li>\
		<li>Lorem ipsum dolor sit amet</li>\
		<li>Lorem ipsum dolor sit amet</li>\
		<li>Lorem ipsum dolor sit amet</li>\
	</ul>\
	<p>\
		Lorem ipsum dolor sit amet, consectetuer adipiscing\
		elit, sed diam nonummy nibh\
	</p>'

f=open('Products_data.txt')
for i in range(5):
	x=f.readline()
	cat_name,y=x.split('|')
	subcategories=y.split(',')
	category= ProductCategory(
		name=cat_name
		)
	db.session.add(category)
	db.session.commit()
	for subcategory in subcategories:
		if '[' in subcategory:
			name,items=subcategory.strip().strip(']').split('[')
			sub_category= ProductSubCategory(
				category=category.id,
				name=name
				)
			db.session.add(sub_category)
			db.session.commit()
			for item in items.split('-'):
				sub_category_item= ProductSubCategoryItems(
					sub_category=sub_category.id,
					name=item,
					image='/images/'+'_'.join(item.lower().split())+".png",
					description=desc
					)
				db.session.add(sub_category_item)
				db.session.commit()
		else:
			name=subcategory.strip()
			sub_category= ProductSubCategory(
				category=category.id,
				name=name
				)
			db.session.add(sub_category)
			db.session.commit()
			item=name
			sub_category_item= ProductSubCategoryItems(
				sub_category=sub_category.id,
				name=item,
				image='/images/'+'_'.join(item.lower().split())+".png",
				description=desc
				)
			db.session.add(sub_category_item)
			db.session.commit()
