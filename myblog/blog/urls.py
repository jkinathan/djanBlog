from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^/$", views.PostListView.as_view(), name="index"),
    url(r"^/about", views.About.as_view(), name="about"),
    path("/",views.PostListView.as_view(),name="post_list"),
    path("/post/<int:pk>",views.PostDetailView.as_view(),name="post_detail"),
    path("/post/new/",views.CreatePostView.as_view(),name="post_create"),
    path("/post/update/<int:pk>",views.PostUpdateView.as_view(),name="post_edit"),
    path("/post/delete/<int:pk>",views.PostDeleteView.as_view(),name="post_delete"),
    path("/post/publish/<int:pk>",views.post_publish,name="post_publish"),
    path("/post/draft/",views.DraftListView.as_view(),name="drafts"),
    path("/post/comment/<int:pk>",views.add_comment_to_post,name="add_comment_post"),
    path("/post/comment/approve/<int:pk>",views.comment_approve,name="comment_approve"),
    path("/post/comment/remove/<int:pk>",views.comment_remove,name="comment_delete"),
    path("/post/comment/publish/<int:pk>",views.post_publish,name="comment_publish"),
]
