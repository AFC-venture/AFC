from app.models import *

page1 = AfcPages(page="Home",sections="HomeBanner,HomeAboutUsSection,HomeAboutUsSectionIcons,RecentProjects,Testimonial,OurClients")
page2 = AfcPages(page="About Us",sections="AboutUsBanner,AboutUsSection,AboutUsSectionIcons,MissionVision,OurTeam,Infrastructure,OurClients")

db.session.add_all([page1,page2])
db.session.commit()