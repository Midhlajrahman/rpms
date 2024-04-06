from .models import CourseCategory

def main_context(request):
    course_categories = CourseCategory.objects.all()

    context = {
        "header_course": course_categories,
    }
    return context