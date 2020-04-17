from django.urls import url, path
from . import views

urlpatterns = [
    #url(r"^/$", views.About.as_view(), name="index"),
    path("/about", views.About.as_view(), name="aboutus"),
    path("/",views.PostListView.as_view(),name="post_list"),
    path("/post/<int:post_id>",views.PostDetailView.as_view(),name="blog_detail"),
    path("/post/create/",views.PostCreateView.as_view(),name="post_create"),
    path("/post/update/<int:post_id",views.PostUpdateView.as_view(),name="post_update"),
]
