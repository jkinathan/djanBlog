from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView)
from .models import Post, Comment
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm

# Create your views here.

class About(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post
    
    #getting the contents of the models
    def get_queryset(self):#pythony version of writing a sqlquery , grab the Post model and all objects there and filter
        return Post.objects.filter(published_date__lte=timezone.now().order_by('-published_date')) #-publis... is for descending order and this is all orm
        #__lte is lessthanOrEqualto
        
        
class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = "blog/post_detail.html"
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Post
    redirect_field_name = "blog/post_detail.html"
    form_class = PostForm