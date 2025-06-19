from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post  # Import the Post model
# Create your views here.
class PostListView(ListView):
    model = Post  # Specify the model to use
    template_name = 'blog/post_list.html'  # Specify the template to use
    context_object_name = 'posts'  # Specify the context variable name
        
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['user_id'] = self.request.session.get('user_id')
        context['username'] = self.request.session.get('username')
        return context


class PostDetailView(DetailView):
    model = Post  # Specify the model to use
    template_name = 'blog/post_detail.html'  # Specify the template to use
    context_object_name = 'post'  # Specify the context variable name

class PostCreateView(CreateView):
    model = Post  # Specify the model to use
    template_name = 'blog/post_form.html'  # Specify the template to use
    fields = ['title', 'content']  # Specify the fields to include in the form
    success_url = '/blog'  # Redirect to the post list after successful creation

class PostUpdateView(UpdateView):
    model = Post  # Specify the model to use
    template_name = 'blog/post_form.html'  # Specify the template to use
    fields = ['title', 'content']  # Specify the fields to include in the form
    success_url = '/blog'  # Redirect to the post list after successful update

class PostDeleteView(DeleteView):
    model = Post  # Specify the model to use
    # 삭제를 시도할때 template_name을 지정 ,get방식으로 호출이 되어야만 해당 html이 렌더링됨
    # post로 요청하면 삭제가 진행됨
    # template_name = 'blog/post_confirm_delete.html'  # Specify the template to use
    success_url = '/blog'  # Redirect to the post list after successful deletion