from django.shortcuts import render
from courses.models import Course


def index(request):
    template_name = 'courses/index.html'
    courses = Course.objects.all()

    return render(request, template_name, {'courses': courses})


# def list_courses(request):
#     courses = Course.objects.all()
#     template_name =
#     return