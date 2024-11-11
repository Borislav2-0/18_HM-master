from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def function_request(request):
    return render(request, "second_task/func_temp.html")


class RequestClass(TemplateView):
    template_name = "second_task/class_temp.html"
