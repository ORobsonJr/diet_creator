from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.decorators.http import require_POST

# Create your views here.
class GetInfos(TemplateView):
    template_name = 'index.html'

@require_POST
def post_form(request):
    if request.method =='POST':
        #Process gender checkboxes
        gender = request.POST.get('gender')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        age = request.POST.get('age')
        activity_level = request.POST.get('activity_level')


        #Run something

        return HttpResponse(200)
    
    return HttpResponse(500)

