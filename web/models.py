from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse_lazy
from easy_thumbnails.fields import ThumbnailerImageField



# Create your models here.

class CourseCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    order = models.IntegerField(default=0)

    def get_course(self):
        return Course.objects.filter(category=self)
    
    def subcategory(self):
        return CourseSubcategory.objects.filter(category=self)
    
    
    class Meta:
        ordering = ["order"]
        verbose_name = ('Categories')
        verbose_name_plural = ('Categories')
        

    def __str__(self):
        return self.name


class CourseSubcategory(models.Model):
    category=models.ForeignKey("web.CourseCategory",on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    

    class Meta:
        verbose_name = ('Course Subcategory')
        verbose_name_plural = ('Course Subcategories')
    
    def get_course(self):
        return Course.objects.filter(subcategory=self)
    
    def __str__(self):
        return self.name
    

class Course(models.Model):
    category = models.ForeignKey(
        "web.CourseCategory",
        verbose_name="course Category",
        related_name="course_category",
        on_delete=models.CASCADE,
    )
    subcategory = models.ForeignKey(
        "web.CourseSubcategory",
        verbose_name="course subcategory",
        related_name="course_subcategory",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = ThumbnailerImageField(
        upload_to="media/",
    )
    order=models.IntegerField(default=1)
    description = HTMLField()

    # cariculum = HTMLField(null=True, blank=True)
      
    
    def get_include(self):
        return Instructor.objects.filter(course=self)
    
    def get_absolute_url(self):
        return reverse_lazy('web:course_detail', kwargs={'slug': self.slug})
    

    def __str__(self):
       return self.title
    
    
class CourseEnquiry(models.Model):
    course = models.ForeignKey(
        "web.Course",
        verbose_name="course",
        related_name="course_enquiry",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField()
    
    
    class Meta:
        verbose_name = ('Course Enquiry')
        verbose_name_plural = ('Course Enquiries')

    def __str__(self):
        return self.name
    
    
class Instructor(models.Model):
    course = models.ForeignKey(
        "web.Course",
        verbose_name="course",
        related_name="course_include",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    image=models.ImageField(upload_to="media/")
    description = models.TextField()

    def __str__(self):
        return self.name


class Testimonial(models.Model):
  image = models.ImageField(upload_to='media')
  name = models.CharField(max_length=255)
  description = models.TextField()


class Career(models.Model):
    image = models.ImageField(upload_to='media',help_text="recomended size 50x50")
    title = models.CharField(max_length=255)
    slug=models.SlugField(unique=True)
    description = HTMLField()
    
    def __str__(self):
        return self.title
    


class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class CarreerEnquiry(models.Model):
    EXPERIENCE=[
        ('Less Then 1 Year', 'Less Then 1 Year'),
        ('1 Year', '1 Year'),
        ('2 Year', '2 Year'),
        ('3 + Year', '3 + Year'),
        
    ]
    WORK=[
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
    ]
    YESNO=[
        ('YES','Yes'),
        ('NO','No'),
    ]
    HEAR=[
        ('Social Media', 'Social Media'),
        ('Friend', 'Friend'),
        ('Others', 'Others'),
    ]
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    career=models.ForeignKey("web.Career",on_delete=models.CASCADE)
    job_role=models.ForeignKey("web.Course",on_delete=models.CASCADE)
    willing_to_work=models.CharField(max_length=255,choices=WORK)
    currently_employed=models.CharField(max_length=255,choices=YESNO)
    qualification=models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    hear_about_us=models.CharField(max_length=255,choices=HEAR)
    cv = models.FileField(upload_to="media")
    
    
    class Meta:
        verbose_name = ('Carreer Enquiry')
        verbose_name_plural = ('Carreer Enquiries')
    
    def __str__(self):
        return self.name
    

    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class DemoRegister(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Team(models.Model):
    order = models.IntegerField(unique=True,blank=True,null=True)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    small_image = ThumbnailerImageField(
        upload_to="team/",help_text="recomended size 100x100"
    )
    big_image = ThumbnailerImageField(
        upload_to="team/",help_text="recomended size 250x350"
    )
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order']
        
        

class DemoVideo(models.Model):
    url=models.TextField(null=True,blank=True,help_text="past embed url here")
    image = models.ImageField(upload_to="media/",null=True,blank=True)
