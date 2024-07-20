from django.http import HttpResponse
from django.template import loader


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # template = loader.get_template('myapp/myfirst.html')
    return HttpResponse("Hello wordl")
    # return HttpResponse(template.render())