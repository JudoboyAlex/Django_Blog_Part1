from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from blog.models import Article, Comment
from datetime import date
from django.views.decorators.http import require_http_methods

def home_page(request):
    current_date = date.today()
    context = {'articles': Article.objects.filter(draft=False).order_by('-published_date'),
               'date': current_date 
                }
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def root_path(request):
    return HttpResponseRedirect('/home')

def blog_display(request, id):
    blog = Article.objects.get(pk=id)
    context = {'blog': blog}
    return render(request, 'blog.html', context)

@require_http_methods(['POST'])
def create_comment(request):
    print(request.POST)
    user_name = request.POST['name']
    user_message = request.POST['message']
    blog_id = request.POST['blog_id']
    blog = Article.objects.get(id=blog_id)
    Comment.objects.create(name=user_name, message= user_message, blog_comment= blog )   
    return redirect('blog_details', id=blog_id)
   