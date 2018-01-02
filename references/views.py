from django.shortcuts import render, redirect
from django.views import View
from .models import Reference
from django.http import HttpResponse

# Create your views here.
def home(request):

    references = Reference.objects.order_by('-pub_date')
    tags = [list(map(str.strip, reference.tags.split(','))) for reference in references]

    return render(request, 'references/home.html', {'info': zip(references, tags)})

class Search(View):
    def get(self, request):
        return HttpResponse("OOOOH Shit")