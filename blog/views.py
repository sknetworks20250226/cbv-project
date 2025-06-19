from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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

class PostCreateView(CreateView):
    model = Post  # Specify the model to use
    template_name = 'blog/post_form.html'  # Specify the template to use
    fields = ['title', 'content']  # Specify the fields to include in the form
    success_url = '/'  # Redirect to the post list after successful creation

class PostUpdateView(UpdateView):
    model = Post  # Specify the model to use
    template_name = 'blog/post_form.html'  # Specify the template to use
    fields = ['title', 'content']  # Specify the fields to include in the form
    success_url = '/'  # Redirect to the post list after successful update

class PostDeleteView(DeleteView):
    model = Post  # Specify the model to use
    template_name = 'blog/post_confirm_delete.html'  # Specify the template to use
    success_url = '/'  # Redirect to the post list after successful deletion