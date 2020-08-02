from django.urls import path
from .views import (
    post_list_view,
    post_detail_view,
    category_view
)

app_name = 'posts'
urlpatterns = [
    path('', post_list_view, name="posts"),
    path('<int:id>', post_detail_view, name="post-detail"),
    path('<str:category>', category_view, name="post-category")
]
