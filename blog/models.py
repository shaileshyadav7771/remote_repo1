from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='Published')

class Post(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('Published','Published'))
    title = models.CharField(max_length=264)
    slug = models.SlugField(max_length=264, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.DO_NOTHING)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)  # datetime when first time object created
    updated = models.DateTimeField(auto_now=True)  # datetme
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects=CustomManager()
    #####for tagging###
    tags=TaggableManager()# i want to associate every post so here TaggableManager will take care of this.
    # Post.tags.all()#Return all post associated with tag.instead of object we are using tag and TagableManager is responsible to associate it.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.publish.year, self.publish.strftime('%m'), self.publish.strftime('%d'),self.slug])

######Model related to comment
# We required to create a Model to save comments
# We required to create a model based form to submit comments
# We required to create a view function to process comments and save to the database
# We have to edit post_detail.html to display list of comments and add a form to submit
# comments
class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=32)
    email=models.EmailField()
    body=models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    #now order we can define.

    class Meta:
        ordering=('-created',)

    #now let me take str if any person want to display comment object.
    def __str__(self):
        return 'Commented by {} on {}'.format(self.name,self.post)
    #Means if any person want to display my comment object sir simply return o/p in above form :)
#Now after creating comment model we need to run migration and migrate and need to register inside admin.py



