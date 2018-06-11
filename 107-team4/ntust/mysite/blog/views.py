from __future__ import unicode_literals
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post,Category,Comment
from . import models
import datetime
from django.utils import timezone


# Create your views here.
def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    categories = Category.objects.all()
    return render(request, 'blog/HOME.html', {'posts': posts, 'categories': categories})

def category(request):
    pid=request.GET["id"]
    posts = Post.objects.filter(category=pid).order_by('-published_date')
    category_this = Category.objects.filter(c_id=pid)
    categories = Category.objects.all()
    return render(request, 'blog/category.html', {'posts': posts,'categories':categories,'category_this':category_this })

def view(request):

    pid=request.GET["id"]
    posts = Post.objects.filter(p_id = pid)
    comments_list = Comment.objects.filter(post = pid)
    categories = Category.objects.all()

    return render(request, 'blog/post_view.html', {'posts': posts,'comments_list':comments_list,'pid':pid,'categories':categories})

def post_comment(request,p_id):
    pid=p_id
    c_title =request.POST['c_title']
    c_user_name = request.POST['c_user_name']
    c_content = request.POST['c_content']
    c_pub_date = timezone.now()
    comment = models.Comment(title=c_title,user_name=c_user_name,content=c_content,pub_date=c_pub_date,post=pid)
    comment.save()
    return HttpResponseRedirect('/blog/view/?id=%s'%pid)

def about(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    categories = Category.objects.all()
    return render(request, 'blog/about.html', {'posts': posts, 'categories': categories})



