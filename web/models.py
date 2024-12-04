from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse_lazy
from easy_thumbnails.fields import ThumbnailerImageField

# Create your models here.

class Service(models.Model):
    service_name = models.CharField(max_length=120)
    service_image = models.ImageField(upload_to="service-images/", blank=True, null=True)
    service_icon = models.FileField(upload_to="service_icons/", max_length=100)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    content = HTMLField(blank=True,null=True)
    class Meta:
        ordering = ("id",)
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def get_absolute_url(self):
        return reverse_lazy("web:service_details", kwargs={"slug": self.slug})

    def get_faq(self):
            return ServiceFaq.objects.filter(service=self)

    def __str__(self):
        return str(self.service_name)


class ServiceEnquiry(models.Model):
    service = models.ForeignKey("web.Service", on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    mobile = models.CharField(max_length=120, blank=True, null=True)
    message = models.TextField()

    class Meta:
        verbose_name = 'Service Enquiry'
        verbose_name_plural = 'Service Enquiries'

    def __str__(self):
        return str(self.name)

class ServiceFaq(models.Model):
    service = models.ForeignKey("web.Service", on_delete=models.CASCADE, blank=True, null=True)
    question = models.CharField(max_length=255)
    answer = HTMLField(blank=True,null=True)

    class Meta:
        ordering = ("id",)
        verbose_name = 'Service FAQ'
        verbose_name_plural = 'Service FAQs'

    def __str__(self):
        return str(self.question)


class Blog(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to="blog-images/",)
    content = HTMLField()

    def get_absolute_url(self):
        return reverse_lazy("web:blog_details", kwargs={"slug": self.slug})

    class Meta:
        ordering = ("date",)
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return str(self.title)


class Team(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150,blank=True,null=True)
    image = models.ImageField(blank=True,null=True, upload_to="team-images",)
    order = models.PositiveIntegerField(default=0)


    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
        ordering = ['order']  

    def __str__(self):
        return str(self.name)


class Testimonials(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    image = models.ImageField(blank=True,null=True, upload_to="testimonial-images",)
    description = models.TextField(blank=True,null=True)

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return str(self.name)


class Contact(models.Model):
    name = models.CharField(max_length=120)
    timestamp = models.DateTimeField(db_index=True,auto_now_add=True)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=120,blank=True,null=True)
    subject = models.CharField(max_length=120,blank=True,null=True)
    message = models.TextField()

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return str(self.name)
    

class Banner(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="slider")
    description = models.TextField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',) 
        verbose_name = ('Banner')
        verbose_name_plural = ('Banners')


class Meta(models.Model):
    PAGES = (
        ('home', "Home"),
        ('about', "About"),
        ('service', "Service"),
        ('blog', "Blog"),
        ('contact_us', "Contact Us"),
        
    )
    page = models.CharField(max_length=20, choices=PAGES,)
    meta_title = models.CharField(max_length=60)
    meta_description = models.CharField(max_length=180)
    meta_keyword = models.CharField(max_length=180)
    canonical_url = models.URLField(blank=True,null=True)
    image = models.ImageField(upload_to="meta_image/",blank=True,null=True)
    
    class Meta:
        ordering = ('-id',)
        verbose_name = "Meta" 
        verbose_name_plural = "Metas"
    
    def __str__(self):
        return self.meta_title
    

class CoreInfo(models.Model):
    whychoose_title = models.CharField(max_length=120)
    whychoose_us = HTMLField()
    our_vision = HTMLField()
    our_mission = HTMLField()
    core_value = HTMLField()
    
    class Meta:
        ordering = ('-id',)
        verbose_name = "Core Info" 
        verbose_name_plural = "Core Infos"
    
    def __str__(self):
        return self.whychoose_title


class AboutUs(models.Model):
    title = models.CharField(max_length=120)
    description = HTMLField()
    image = models.ImageField(upload_to="about_us/",blank=True,null=True)
    
    def get_points(self):
        return AboutPoint.objects.filter(about_us=self)
    
    class Meta:
        ordering = ('-id',)
        verbose_name = "About Us" 
        verbose_name_plural = "About Us"
    
    def __str__(self):
        return self.title
    

class AboutPoint(models.Model):
    about_us = models.ForeignKey("web.AboutUs", on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    
    class Meta:
        ordering = ('-id',)
        verbose_name = "About Point" 
        verbose_name_plural = "About Points"
    
    def __str__(self):
        return self.title
    
    

class FAQ(models.Model):
    question = models.CharField(max_length=180)
    answer = models.TextField()
    
    class Meta:
        ordering = ('-id',)
        verbose_name = "FAQ" 
        verbose_name_plural = "FAQs"
        
    
    def __str__(self):
        return self.question
    
    
class Insights(models.Model):
    icon = models.FileField(upload_to="insights/")
    title = models.CharField(max_length=120)
    description = models.TextField()
    
    class Meta:
        ordering = ('-id',)
        verbose_name = "Insight" 
        verbose_name_plural = "Insights"
    
    def __str__(self):
        return self.title
    
    
class Industries(models.Model):
    icon = models.FileField(upload_to="industries/")
    title = models.CharField(max_length=120)
    description = models.TextField()
    
    class Meta:
        ordering = ('-id',)
        verbose_name = "Industry" 
        verbose_name_plural = "Industries"
    
    def __str__(self):
        return self.title
    

class MarqueeText(models.Model):
    title = models.CharField(max_length=120)
    
    class Meta:
        ordering = ('-id',)
        verbose_name = "Marquee Text" 
        verbose_name_plural = "Marquee Texts"
    
    def __str__(self):
        return self.title
    

class RPMSKonnect(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to="rpms_konnect/",blank=True,null=True)
    pdf = models.FileField(upload_to="rpms_konnect/",blank=True,null=True)
    
    class Meta:
        ordering = ('-id',)
        verbose_name = "RPMS Konnect" 
        verbose_name_plural = "RPMS Konnects"
    
    def __str__(self):
        return self.title