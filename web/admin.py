from django.contrib import admin
from .models import Team
from .models import Service
from .models import Blog
from .models import Testimonials
from .models import Contact
from .models import ServiceEnquiry
from .models import ServiceFaq

# Register your models here.

class ServiceFaqInline(admin.TabularInline):
    model = ServiceFaq
    fields = ('question','answer')
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name',)
    prepopulated_fields = {'slug':('service_name',)}
    inlines = [ServiceFaqInline]

@admin.register(ServiceEnquiry)
class ServiceEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name','email',)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name','position',)
    prepopulated_fields = {'slug':('name',)}

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug':('title',)}

@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('name','position',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email',)