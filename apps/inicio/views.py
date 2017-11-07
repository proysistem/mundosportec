#from libs.views import CachedViewMixin
from django.shortcuts import render
from django.views.generic import TemplateView
# from .models import Page

#class IndexView(TemplateView):
#    template_name = 'inicio/index.html'
#    config = None

def home(request):
    context = {}
    template = 'inicio/index.html'
    return render(request, template, context)