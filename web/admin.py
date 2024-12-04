from django.contrib import admin
from .models import Team
from .models import Service
from .models import Blog
from .models import Testimonials
from .models import Contact
from .models import ServiceEnquiry
from .models import ServiceFaq, Banner, Meta, AboutUs, AboutPoint, CoreInfo, FAQ, Insights, Industries, MarqueeText, RPMSKonnect

# Register your models here.

class ServiceFaqInline(admin.TabularInline):
    model = ServiceFaq
    fields = ('question','answer')
    extra = 1


class AboutPointInline(admin.TabularInline):
    model = AboutPoint
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

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug':('title',)}

@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email',)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("title","is_active",)
    search_fields = ("title",)


@admin.register(Meta)
class MetaAdmin(admin.ModelAdmin):
    list_display = ("meta_title", "page")
    

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    inlines = [AboutPointInline]
    

@admin.register(CoreInfo)
class CoreInfoAdmin(admin.ModelAdmin):
    list_display = ("whychoose_title",)
    

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question",)
    

@admin.register(Insights)
class InsightsAdmin(admin.ModelAdmin):
    list_display = ("title",)
    

@admin.register(Industries)
class IndustriesAdmin(admin.ModelAdmin):
    list_display = ("title",)
    

@admin.register(MarqueeText)
class MarqueeTextAdmin(admin.ModelAdmin):
    list_display = ("title",)
    

@admin.register(RPMSKonnect)
class RPMSKonnectAdmin(admin.ModelAdmin):
    list_display = ("title",)