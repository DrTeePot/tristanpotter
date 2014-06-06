from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from blog.models import Post, Comment

# Create your views here.

def index(request):

    #posts = Post.objects.order_by('-time_created')[:5]

    return render(request,
                  'blog/index.html',
                  {'posts': None})


def filter_posts(request):
    pass


def view_post(request, post_id):

    try:
        post = Post.objects.get(pk = post_id)
    except:
        return HttpResponseRedirect('/blog/')


    return render(request,
                  'blog/post.html',
                  {'post' : post}) #post if valid, none if not


def comment(request, post_id):
    pass


def register(request):
    pass


def view_account():
    pass