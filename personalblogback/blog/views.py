from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from blog.models import Article
import json


def start(request):
    return JsonResponse({'status': "success"})


@csrf_exempt
def senddata(request):
    data = list(Article.objects.all())

    jdata = []
    for q in data:
        jdata.append({'Title': q.title, 'Content': q.content})
    return JsonResponse({'status': "success", "data": jdata})


@csrf_exempt
def postdata(request):
    title = request.POST.get('title')
    content = request.POST.get('text')
    o = Article(title=title, content=content)
    o.save()
    return JsonResponse({'status': "success"})
