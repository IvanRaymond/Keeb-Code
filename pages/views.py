from django.shortcuts import render, get_object_or_404
from .models import Profile
from posts.models import Post
from .form import ContactForm
from django.core.mail import send_mail


# Create your views here.


def feed_view(request):
    queryset = Post.objects.all()
    context = {
        "post_list": queryset
    }
    return render(request, "feed.html", context)


def about_view(request):
    obj = get_object_or_404(Profile, id=1)
    context = {
        "profile": obj
    }
    return render(request, "about.html", context)


def contact_view(request):
    form = ContactForm(request.POST or None)
    success = False
    if form.is_valid():
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        sent_messages = send_mail(
            'Message on Keeb&Code from ' + str(name),
            "<" + str(message) + "> reply to " + str(email),
            str(email),
            ['nestaray@hotmail.com'],
        )
        
        form = ContactForm()
        if sent_messages == 1:
            success = True

    context = {
        'form': form,
        'success': success
    }
    return render(request, "contact.html", context)


def handler400(request, exception):
    return render(request, '400.html', status=400)


def handler403(request, exception):
    return render(request, '403.html', status=403)


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
