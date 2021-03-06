"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import home_page, root_path, blog_display, create_comment, article, login_view, logout_view, signup,blog_edit_view, blog_delete_view


urlpatterns = [
    path('', root_path),
    path('admin/', admin.site.urls),
    path('home/', home_page, name="home"),
    path('home/<int:id>', blog_display, name='blog_details'),
    path('comments/new/', create_comment, name='create_comment'),
    path('home/article', article, name='articles' ),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('signup/', signup, name='signup'),
    path('home/<int:id>/update/', blog_edit_view, name='update'),
    path('home/<int:id>/delete', blog_delete_view, name='delete'),
]
