from app.models import *

# page1 = AfcPages(page="Home",sections="HomeBanner,HomeAboutUsSection,HomeAboutUsSectionIcons,RecentProjects,Testimonial,OurClients")
# page2 = AfcPages(page="About Us",sections="AboutUsBanner,AboutUsSection,AboutUsSectionIcons,MissionVision,OurTeam,Infrastructure,OurClients")

# db.session.add_all([page1,page2])


icon1 = HomeAboutUsSectionIcons.query.filter_by(description="Inhouse<br>Manufacturing").first()
icon1.static_image="/icons/warehouse-static.png"
icon1.hover_image="/icons/warehouse-hover.png"
icon2 = HomeAboutUsSectionIcons.query.filter_by(description="Customisation<br>Capability").first()
icon2.static_image="/icons/customisation-static.png"
icon2.hover_image="/icons/customisation-hover.png"
icon3 = HomeAboutUsSectionIcons.query.filter_by(description="Pan-India<br>Presence").first()
icon3.static_image="/icons/PANIndia-static.png"
icon3.hover_image="/icons/PANIndia-hover.png"
icon4 = HomeAboutUsSectionIcons.query.filter_by(description="Environmentally<br>Responsible").first()
icon4.static_image="/icons/environmentally_responsible-static.png"
icon4.hover_image="/icons/environmentally_responsible-hover.png"
icon5 = HomeAboutUsSectionIcons.query.filter_by(description="Trusted Over<br>12 Years").first()
icon5.static_image="/icons/truster_over_12years-static.png"
icon5.hover_image="/icons/truster_over_12years-hover.png"
icon6 = HomeAboutUsSectionIcons.query.filter_by(description="Make in<br>India").first()
icon6.static_image="/icons/makeinindia-static.png"
icon6.hover_image="/icons/makeinindia-hover.png"
print(icon1)
db.session.commit()