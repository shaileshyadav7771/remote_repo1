from blog.models import Post
from django import template#import template
register=template.Library()#registered it inside library
from django.db.models import Count

@register.simple_tag # due to tis it become simple tag.
def total_posts():      # name of simple tag will be total_posts if we want we can defined our custom name.
    return Post.objects.count()

#####note: tommorow if i dont want to use total_posts so no problem we can pass our
# custom name def total_posts(name=shailesh)


@register.inclusion_tag('blog/latest_post123.html')
def show_latest_posts():
    latest_posts=Post.objects.order_by('-publish')[:5]
    return {'latest_posts':latest_posts}


###############Assignment tag#######################

# @register.simple_tag
# def get_mostcommented_posts(count=5,name='most_commented_posts'):
#     return Post.objects.annotate(total_comments=Count('comments')).order_by('-totalcooments')[:count]
#



# Note: Here in case of inclusion_tag it will returnrender o/p in above latest_post123.html(our own define file.)