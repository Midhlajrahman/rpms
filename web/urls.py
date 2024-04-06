from django.urls import path

from . import views


app_name = "web"


urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('blog/',views.BlogView.as_view(),name='blog'),
    path('services/',views.ServicesView.as_view(),name='services'),
    path('career/<slug:slug>/',views.CareerDetailView.as_view(),name='career_detail'),
    path('contact/',views.ContactView.as_view(),name='contact'),

    path('gallery/',views.GalleryView.as_view(),name='gallery'),
]