from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post  # Import the Post model
# Create your views here.
class PostListView(ListView):
    model = Post  # Specify the model to use
    template_name = 'blog/post_list.html'  # Specify the template to use
    context_object_name = 'posts'  # Specify the context variable name

class PostDetailView(DetailView):
    model = Post  # Specify the model to use
    template_name = 'blog/post_detail.html'  # Specify the template to use
    context_object_name = 'post'  # Specify the context variable name