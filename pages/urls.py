from django.urls import path
from .views import (
    feed_view,
    about_view,
    contact_view
)

app_name = 'pages'
urlpatterns = [
    path("", feed_view, name='feed'),
    path("about/", about_view, name='about'),
    path("contact/", contact_view, name='contact')
]
