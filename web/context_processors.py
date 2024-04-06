from .models import Service

def main_context(request):
    service = Service.objects.all()

    context = {
        "services": service,
    }
    return context