from django.shortcuts import render, get_object_or_404
from .models import Post
from pages.models import Profile

# Create your views here.


def post_list_view(request):
    queryset = Post.objects.all()
    peripheral = False
    programming = False
    experiences = False
    hardware = False
    software = False

    for post in queryset:
        if post.visible:
            if post.category == 'peripheral':
                peripheral = True
            elif post.category == 'programming':
                programming = True
            elif post.category == 'experiences':
                experiences = True
            elif post.category == 'hardware':
                hardware = True
            elif post.category == 'software':
                software = True

    context = {
        'programming': programming,
        'peripheral': peripheral,
        'experiences': experiences,
        'hardware': hardware,
        'software': software
    }
    return render(request, "post_list.html", context)


def post_detail_view(request, id):
    obj = get_object_or_404(Post, id=id)
    profile = Profile.objects.get(id=1)
    context = {
        "object": obj,
        "profile": profile
    }
    return render(request, "post_detail.html", context)


def category_view(request, category):
    queryset = Post.objects.all()
    sorted_posts = []
    for post in queryset:
        if post.category == category:
            sorted_posts.append(post)

    context = {
        'post_list': sorted_posts,
        'category': category
    }
    return render(request, "post_category.html", context)
