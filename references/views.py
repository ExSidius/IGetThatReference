from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import Reference
# from django.http import HttpResponse

# Create your views here.
def home(request):

    references = Reference.objects.order_by('-pub_date')
    tags = [list(map(str.strip, reference.tags.split(','))) for reference in references]

    context = {'info': zip(references, tags)}

    return render(request, 'references/home.html', context)

def tag(request, tag_name):

    references = [reference for reference in Reference.objects.order_by('-pub_date') if tag_name in reference.tags]
    tags = [list(map(str.strip, reference.tags.split(','))) for reference in references]

    context = {
                'type': 'tag',
                'info': zip(references, tags),
                'input': tag_name
            }

    return render(request, 'references/tagsearch.html', context)

def search(request, search_param):

    references = [reference for reference in Reference.objects.order_by('-pub_date') if search_param in reference.tags]
    tags = [list(map(str.strip, reference.tags.split(','))) for reference in references]

    context = {
                'type': 'search',
                'info': zip(references, tags),
                'input': search_param
            }

    return render(request, 'references/tagsearch.html', context)