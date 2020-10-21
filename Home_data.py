from app.models import *

banner = HomeBanner(title="Reimagining Workspaces",image="images/Slider02.png")
db.session.add(banner)
db.session.commit()

about = HomeAboutUsSection(content="AFC Furniture Solutions is the fastest growing brand in the office furniture manufacturing industry that started in 2008. AFC is an\
end-to-end solution company with Green Manufacturing setup spread across 1.5 lakh sq ft. and capability to manufacture 10k\
workstations and 8k chairs in a month. Manufacturing setup in Delhi-NCR region, team of 60+ passionate professionals and a\
skilled workforce of 300+, AFC has a pan-India presence with branch offices in Mumbai and Delhi-NCR region. Having gained\
experience of more than a decade in Design and Manufacturing, AFC boasts of the shortest delivery timeline and has been\
successful in retaining more than 93\% clients since inception. Product Portfolio - AFC can customise solutions as per client\
requirements and specialise in manufacturing Workstations, Cabins, Seating Solutions, Lose Furniture, Storage, Educational,\
Laboratories and more. The company takes pride in conveying that all their products and solutions are manufactured in India.")
db.session.add(about)
db.session.commit()

icon1 = HomeAboutUsSectionIcons(section=about.id,description="Inhouse<br>Manufacturing",static_image="warehouse-static",hover_image="warehouse-hover")
icon2 = HomeAboutUsSectionIcons(section=about.id,description="Customisation<br>Capability",static_image="customisation-static",hover_image="customisation-hover")
icon3 = HomeAboutUsSectionIcons(section=about.id,description="Pan-India<br>Presence",static_image="PANIndia-static",hover_image="PANIndia-hover")
icon4 = HomeAboutUsSectionIcons(section=about.id,description="Environmentally<br>Responsible",static_image="environmentally_responsible-static",hover_image="environmentally_responsible-hover")
icon5 = HomeAboutUsSectionIcons(section=about.id,description="Trusted Over<br>12 Years",static_image="truster_over_12years-static",hover_image="truster_over_12years-hover")
icon6 = HomeAboutUsSectionIcons(section=about.id,description="Make in<br>India",static_image="makeinindia-static",hover_image="makeinindia-hover")
db.session.add_all([icon6,icon5,icon4,icon3,icon2,icon1])
db.session.commit()

ProductCategory.query.filter_by(name="Workstations").first().image="/images/workstation.png"
ProductCategory.query.filter_by(name="Tables").first().image="/images/tables.png"
ProductCategory.query.filter_by(name="Storage").first().image="/images/storgae.png"
ProductCategory.query.filter_by(name="Seating").first().image="/images/seating.png"
ProductCategory.query.filter_by(name="Educational").first().image="/images/educational.png"
db.session.commit()

project1 = RecentProjects(description="Concentrix",image="images/Concentrix.png")
project2 = RecentProjects(description="Tokopedia",image="images/Tokopedia.png")
project3 = RecentProjects(description="India Mart",image="images/India_Mart.png")
project4 = RecentProjects(description="HCL",image="images/HCL_Nagpur.png")
project5 = RecentProjects(description="ABC",image="images/workstation.png")
project6 = RecentProjects(description="XYZ",image="images/cabins.png")
db.session.add_all([project6,project5,project4,project3,project2,project1])
db.session.commit()

testimonial="AFC is very professional and<br>up to their promise."
testimonial1 = Testimonial(client_name="IndiaMart",client_logo="clients/testimonial_indiamart.png",testimonial=testimonial);
testimonial2 = Testimonial(client_name="MaxLife",client_logo="clients/testimonial_maxlife.png",testimonial=testimonial);
testimonial3 = Testimonial(client_name="R1",client_logo="clients/testimonial_R1.png",testimonial=testimonial);
testimonial4 = Testimonial(client_name="HCL",client_logo="clients/testimonial_hcl.png",testimonial=testimonial);
testimonial5 = Testimonial(client_name="Advant",client_logo="clients/testimonial_advant.png",testimonial=testimonial);
testimonial6 = Testimonial(client_name="AIHP",client_logo="clients/testimonial_aihp.png",testimonial=testimonial);
testimonial7 = Testimonial(client_name="AXIS",client_logo="clients/testimonial_axis.png",testimonial=testimonial);
db.session.add_all([testimonial6,testimonial5,testimonial4,testimonial3,testimonial2,testimonial1,testimonial7])
db.session.commit()
