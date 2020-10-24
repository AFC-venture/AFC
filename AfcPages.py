from app.models import *

page1 = AfcPages(priority=1,page="Home",sections="HomeBanner,HomeAboutUsSection,HomeAboutUsSectionIcons,RecentProjects,Testimonial,OurClients")
page2 = AfcPages(priority=1,page="About Us",sections="AboutUsBanner,AboutUsSection,AboutUsSectionIcons,MissionVision,OurTeam,Infrastructure,OurClients")
page3 = AfcPages(priority=1,page="Products",sections="ProductsBanner,ProductsPromiseSection,ProductCategory")
page4 = AfcPages(page="ProductsSubCategory",sections="ProductSubCategory,ProductSubCategoryItems")
page5 = AfcPages(page="ProductsSubCategoryDetails",sections="ProductSubCategory,ProductSubCategoryItems")
page6 = AfcPages(priority=1,page="Projects",sections="ProjectsBanner")
page7 = AfcPages(page="ProjectsGallery",sections="Testimonial,ProjectsGallery")
page8 = AfcPages(page="AllProjects",sections="AllProjects")
page9 = AfcPages(priority=2,page="Clients",sections="ClientsBanner,AboutClients,AboutClientsCategories,CategoryClients")
page10 = AfcPages(priority=1,page="Latest At AFC",sections="LatestBanner,WhatsNewSection,FridaysAtAfc,FridaysAtAfcImages,SocialMedia")
page11 = AfcPages(priority=1,page="Contact Us",sections="ContactUsBanner,ContactForm,ContactFormFields,ContactInfo")

db.session.add_all([page1,page2,page3,page4,page5,page6,page7,page8,page9,page10,page11])
db.session.commit()
