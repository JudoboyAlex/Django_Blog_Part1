from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Article
from datetime import date

def home_page(request):
    current_date = date.today()
    context = {'articles': Article.objects.filter(draft=False).order_by('-published_date'),
               'date': current_date 
                }
    response = render(request, 'index.html', context)
    return HttpResponse(response)


   