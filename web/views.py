from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView

from .models import Team, Testimonial, Career, Course,CourseCategory,DemoVideo
from .forms import CareerEnquiryForm,ContactForm,DemoRegisterForm,CourseEnquiryForm


def index(request):
    testimonial = Testimonial.objects.all()
    tutions = Career.objects.all()
    coursecategorys = CourseCategory.objects.all()
    courses = Course.objects.all().order_by('order')


    context = {
        "testimonial" : testimonial,
        "tutions" : tutions,
        "course" : courses,
        "coursecategorys" : coursecategorys,
        }
    return render(request, 'web/index.html', context)


def about(request):
    teams = Team.objects.all()
    return render(request, 'web/about.html',{"teams":teams})



class BlogView(ListView):
    model = Career
    template_name = "web/blog.html"


class ServicesView(ListView):
    model = Career
    template_name = "web/services.html"


class GalleryView(ListView):
    model = Career
    template_name = "web/career.html" 
    
    
class DemoRegisterView(FormView):
    form_class = DemoRegisterForm

    def form_valid(self, form):
        form.save()
        response_data = { "status": "true","title": "Successfully submitted","message": "We valued your request for the demo,our team will revert to you at the soonest",}
        return JsonResponse(response_data)

    def form_invalid(self, form):
        response_data = {"status": "false","title": "Form validation error",}
        return JsonResponse(response_data, status=400)
    
    
class DemoImageView(TemplateView):
    template_name = "web/image.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["demos"] = DemoVideo.objects.all()
        return context



def courses(request):
    coursecategorys = CourseCategory.objects.all()
    course = Course.objects.all().order_by('order')
    context={'coursecategorys':coursecategorys,"course":course}
    return render(request, 'web/courses.html',context)


class CourseDetailView(DetailView,FormView):
    model = Course
    form_class = CourseEnquiryForm
    template_name = "web/course-details.html"

    def form_valid(self, form):
        form.save()
        response_data = { "status": "true","title": "Thankyou for your interest with jamia","message": "Your application had submitted successfully.",}
        return JsonResponse(response_data)

    def form_invalid(self, form):
        print(form.errors)
        response_data = {"status": "false","title": "Form validation error",}
        return JsonResponse(response_data, status=400)



class CareerDetailView(DetailView,FormView):
    model = Career
    form_class = CareerEnquiryForm
    template_name = "web/career-details.html"

    def form_valid(self, form):
        form.save()
        response_data = { "status": "true","title": "Successfully submitted","message": "Message successfully updated",}
        return JsonResponse(response_data)

    def form_invalid(self, form):
        print(form.errors)
        response_data = {"status": "false","title": "Form validation error",}
        return JsonResponse(response_data, status=400)



class ContactView(FormView):
    form_class = ContactForm
    template_name = "web/contact.html"

    def form_valid(self, form):
        form.save()
        response_data = { "status": "true","title": "Thankyou for your quirey submitted","message": "our team will revert to you at the earliest ",}
        return JsonResponse(response_data)

    def form_invalid(self, form):
        response_data = {"status": "false","title": "Form validation error",}
        return JsonResponse(response_data, status=400)
