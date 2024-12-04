import urllib.parse
from django.shortcuts import render,redirect
from .models import Team
from .models import Service, ServiceFaq
from .models import Blog,Banner, AboutUs, CoreInfo, FAQ, Insights, Industries, MarqueeText, RPMSKonnect
from .models import Testimonials, Meta
from .forms import ContactForm
from .forms import ServiceEnquiryForm


def index(request):
    meta = Meta.objects.filter(page="home").first()
    services = Service.objects.all()
    blogs =Blog.objects.all().order_by('-date')
    testimonials =Testimonials.objects.all()
    teams = Team.objects.all()
    banners = Banner.objects.filter(is_active=True)
    about_us = AboutUs.objects.first()
    core_info = CoreInfo.objects.first()
    faqs = FAQ.objects.all()
    insights = Insights.objects.all()
    industries = Industries.objects.all()
    marquee_texts = MarqueeText.objects.all()
    rpms_konnects = RPMSKonnect.objects.all()[:3]
    context = {"is_index": True,"services": services,"blogs": blogs,"testimonials": testimonials,"teams": teams, "banners": banners, "meta":meta, "about_us":about_us, "core_info":core_info, "faqs":faqs, "insights":insights, "industries":industries, "marquee_texts":marquee_texts, "rpms_konnects":rpms_konnects }
    return render(request, "web/index.html", context)

def about(request):
    meta = Meta.objects.filter(page="about").first()
    teams = Team.objects.all()
    context = {"is_about": True, "teams": teams, "meta":meta}
    return render(request, "web/about.html", context)


def service(request):
    meta = Meta.objects.filter(page="service").first()
    services =Service.objects.all()
    context = {"is_service": True,"services": services, "meta":meta}
    return render(request, "web/service.html", context)


def service_details(request, slug):
    service = Service.objects.get(slug=slug)
    service_faqs = ServiceFaq.objects.filter(service=service)
    other_services = Service.objects.exclude(slug=slug)

    if request.method == 'POST':
        form = ServiceEnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save(commit=False)
            enquiry.service = service
            enquiry.save()

            message = (
                f"service Name: {enquiry.service}\n"
                f'Name: {form.cleaned_data["name"]} \n'
                f'Phone: {form.cleaned_data["mobile"]}\n'
                f'Email: {form.cleaned_data["email"]}\n'
                f'Message: {form.cleaned_data["message"]}\n'
            )

            whatsapp_api_url = "https://api.whatsapp.com/send"
            phone_number = "+97450788611"
            encoded_message = urllib.parse.quote(message)
            whatsapp_url = f"{whatsapp_api_url}?phone={phone_number}&text={encoded_message}"

            return redirect(whatsapp_url)
        else:
            print(form.errors)
    else:
        form = ServiceEnquiryForm()

    context = {
        "is_service": True,
        "service": service,
        "service_faqs": service_faqs,
        "other_services": other_services,
        "form": form,
    }

    return render(request, "web/services-single.html", context)


def blog(request):
    meta = Meta.objects.filter(page="blog").first()
    blogs =Blog.objects.all().order_by('-date')
    context = {"is_blog": True,"blogs": blogs, "meta":meta}
    return render(request, "web/blog.html", context)


def blog_details(request,slug):
    blog = Blog.objects.get(slug=slug)
    recentposts = Blog.objects.exclude(slug=slug)
    context = {"is_blog": True,"blog": blog,"recentposts": recentposts}
    return render(request, "web/blog-single.html", context)


def contact(request):
    meta = Meta.objects.filter(page="contact_us").first()
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            enquiry = form.save(commit=False)
            enquiry.contact = contact
            enquiry.save()

            message = (
                f'Name: {form.cleaned_data["name"]} \n'
                f'Phone: {form.cleaned_data["phone"]}\n'
                f'Email: {form.cleaned_data["email"]}\n'
                f'Subject: {form.cleaned_data["subject"]}\n'
                f'Message: {form.cleaned_data["message"]}\n'
            )

            whatsapp_api_url = "https://api.whatsapp.com/send"
            phone_number = "+97450788611"
            encoded_message = urllib.parse.quote(message)
            whatsapp_url = f"{whatsapp_api_url}?phone={phone_number}&text={encoded_message}"

            return redirect(whatsapp_url)

    else:
        form = ContactForm()

    context ={"is_contact": True, "form": form, "meta":meta}
    return render(request, "web/contact.html", context)


def handler404(request, exception):
    return render(request, "web/404.html", status=404)