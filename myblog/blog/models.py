from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.PROTECT)
    title = models.CharField(max_length=250)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)# timezone function and not executing it instead
    published_date = models.DateTimeField(blank=True,null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
    
    #after someone has created a post where are they redirected using absolute_url
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
        #goto the detail page of the primary key you just created
    
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments',on_delete=models.PROTECT)
    author = models.CharField(max_length=20)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment = True
        self.save()
    
    def get_absolute_url(self):
        return reverse("post_list", kwargs={"pk": self.pk})
        #take them back to the list of posts created
    
    def __str__(self):
        return self.text