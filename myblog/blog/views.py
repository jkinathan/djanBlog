from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post, Comment
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy

# Create your views here.

#function based view for publishing
@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish() #executing the pulbish method from the models
    return redirect('post_detail',pk=pk)

#class based views
class About(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post
    
    #getting the contents of the models
    def get_queryset(self):#pythony version of writing a sqlquery , grab the Post model and all objects there and filter
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') #-publis... is for descending order and this is all orm
        #__lte is lessthanOrEqualto
        
        

class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'blog/post_form.html'
    login_url = '/login/'
    redirect_field_name = "blog/post_detail.html"
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Post
    redirect_field_name = "blog/post_detail.html"
    form_class = PostForm


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin, ListView):
    
    model = Post
    login_url = '/login/'
    
    redirect_field_name = "blog/post_list.html"
    
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')

#######################################################################
#######################################################################
#these are function based views
@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk = pk) #pass in the post model
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk = post.pk)
    else:
        form = CommentForm()
    return render(request,'blog/comment_form.html', {'form':form}) 

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)