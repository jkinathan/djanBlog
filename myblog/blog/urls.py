from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r"^/$", views.About.as_view(), name="index"),
    path("/about", views.About.as_view(), name="aboutus"),
    path("/",views.PostListView.as_view(),name="post_list"),
    path("/post/<int:post_id>",views.PostDetailView.as_view(),name="blog_detail"),
    path("/post/create/",views.PostCreateView.as_view(),name="post_create"),
    path("/post/update/<int:post_id",views.PostUpdateView.as_view(),name="post_update"),
    path("/post/delete/<int:post_id",views.PostDeleteView.as_view(),name="post_delete"),
    path("/post/draft/",views.DraftListView.as_view(),name="drafts"),
    path("/post/comment/<int:post_id",views.add_comment_to_post,name="add_comment_post"),
]
