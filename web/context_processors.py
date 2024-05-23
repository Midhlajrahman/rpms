from .models import Service

def main_context(request):
    service_banner = Service.objects.all()

    context = {
        "service_banner": service_banner,
    }
    return context