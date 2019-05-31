from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from datetime import date
from django.views.decorators.http import require_http_methods
from blog.forms import ArticleForm
from django.utils import timezone
from blog.models import Article, Comment

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
    user_name = request.POST['name']
    user_message = request.POST['message']
    blog_id = request.POST['blog_comment']
    blog = Article.objects.get(id=blog_id)
    Comment.objects.create(name=user_name, message= user_message, blog_comment= blog )   
    return redirect('blog_details', id=blog_id)

def article(request):
    # Create Article
    current_date = date.today()
    if request.method == "POST":
        form = ArticleForm(request.POST)

        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.published_date = timezone.now()
            article.save()
            return redirect('blog_details', id=article.id)
        else:
            return render(request, 'post_edit.html', {'form':form, 'date': current_date})

    # Viewing an Article
    else:
        form = ArticleForm()
        return render(request, 'post_edit.html', {'form':form, 'date': current_date})


  