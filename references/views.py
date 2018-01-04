from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView

from rest_framework.response import Response
# from rest_framework import status

# from django.views import View
# from django.views.generic import TemplateView, ListView, DetailView
# from django.http import HttpResponse

from .models import Reference
from .serializer import ReferenceSerializer


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



def search(request):

    def search(search_params):
        params = list(map(str.lower, search_params.split()))

        references = []
        for reference in Reference.objects.order_by('-pub_date'):

            quote = reference.quote
            author = reference.author
            source = reference.source
            tags = reference.tags
            mish = (quote + author + source + tags).lower()

            for param in params:
                if (param in mish) and (reference not in references):
                    references.append(reference)

        return references

    if request.method == 'GET':
        search_param = request.GET['params']
        references = search(search_param)
        tags = [list(map(str.strip, reference.tags.split(','))) for reference in references]

        context = {
            'type': 'search',
            'info': zip(references, tags),
            'input': search_param
        }

        return render(request, 'references/tagsearch.html', context)

def unique(request, id):

    references = [Reference.objects.get(pk=id)]
    tags = [list(map(str.strip, reference.tags.split(','))) for reference in references]

    context = {'info': zip(references, tags)}

    return render(request, 'references/home.html', context)


# Lists all stocks and get new one
class ReferenceList(APIView):
    def get(self, request):
        references = Reference.objects.all()
        serialize = ReferenceSerializer(references, many=True)

        return Response(serialize.data)

    def post(self, request):
        pass