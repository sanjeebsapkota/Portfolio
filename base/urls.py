from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .import views 
urlpatterns = [
    path("",views.home, name="home"),
    path("about/",views.about,name="about"),
    path("projects/",views.projects,name="projects"),
    path("experience/", views.experience, name="experience"),
    path("certificate/", views.certificate ,name="certificate"),
    path("contact/", views.contact, name="contact"),
    path("resume/",views.resume, name="resume")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
