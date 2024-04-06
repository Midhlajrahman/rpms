from django.contrib import admin

from .models import  Team, Testimonial, Career, Course, CourseCategory ,Instructor,CarreerEnquiry ,Subject ,Contact,DemoRegister,CourseSubcategory,CourseEnquiry ,DemoVideo

# Register your models here.


class CourseIncludeInline(admin.TabularInline):
    model = Instructor
    extra = 1
    
class CategoryInline(admin.TabularInline):
    model = CourseSubcategory
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","category","order" )
    list_filter = ("category",)
    prepopulated_fields = {"slug": ("title",)}
    # inlines = [CourseIncludeInline]


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)
    inlines = [CategoryInline]
    

@admin.register(CourseSubcategory)
class CourseSubcategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "description",)


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    

@admin.register(CarreerEnquiry)
class CarreerEnquiryAdmin(admin.ModelAdmin):
    list_display = ("name","career", "phone",)
    
    
    
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name",)
    

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    

@admin.register(DemoRegister)
class DemoRegisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    
@admin.register(CourseEnquiry)
class CourseEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'designation',)
    
@admin.register(DemoVideo)
class DemoVideoAdmin(admin.ModelAdmin):
    pass