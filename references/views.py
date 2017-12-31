from django.shortcuts import render, redirect
from .models import Reference

# Create your views here.
def home(request):

    references = Reference.objects.order_by('-pub_date')
    tags = [list(map(str.strip, reference.tags.split(','))) for reference in references]

    return render(request, 'references/home.html', {'info': zip(references, tags)})