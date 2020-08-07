from django.contrib import admin

# Register your models here.
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','publish','created','updated','status']
    list_filter=('status','author','created','publish')
    search_fields=('title','body')
    prepopulated_fields={'slug':('title',)}
    raw_id_fields=('author',)
    # date_hierarchy='publish'
    ordering=['status','publish']
admin.site.register(Post,PostAdmin)

#####admin registration for Comment#####
from blog.models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display=('name','email','post','body','created','updated','active')
    list_filter=('active','created','updated')
    search_filter=('name','email','body')
    #Above all are for admin webpage customization not for end user.:)
admin.site.register(Comment,CommentAdmin)
