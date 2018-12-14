from django.urls import path, re_path, include
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [
    path('blog/', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
                                   template_name="blog/blog.html")),
    re_path('(?P<pk>(\d+))', DetailView.as_view(model=Post,
                                                  template_name='blog/post.html')),

    ]
