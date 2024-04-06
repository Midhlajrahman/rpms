from django.urls import path

from . import views


app_name = "web"


urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about,name='about'),
    path("services/", views.service, name="service"),
    path("service/<slug:slug>/", views.service_details, name="service_details"),
    path("team/<slug:slug>/", views.team, name="team"),
    path("blog/", views.blog, name="blog"),
    path("blogs/<slug:slug>/", views.blog_details, name="blog_details" ),
    path("contact/", views.contact, name="contact"),
]