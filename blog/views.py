from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from taggit.models import Tag
# Create your views here.

def post_list_view(request,tag_slug=None):
    post_list=Post.objects.all()
    tag=None
    if tag_slug:  #Means user is clicking on tag OR selecting.
        tag=get_object_or_404(Tag,slug=tag_slug)#this is tag object.
        post_list=post_list.filter(tags__in=[tag])#filtered post related to particular tag
#for e.g if i click on python tag then slug=python
    paginator=Paginator(post_list,3)#pagination object i hve created.
    page_number=request.GET.get('page')#we will get current page no n this is taking care by paginator module.:)
    # post_list=paginator.page(page_number)
    # page_obj = paginator.get_page(page_number)
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)#we are not sending any request so by default we hve to display first page
    #now we we don't have next page then we will get empty n need to display last page.
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)# for last page we need to use num_pages inbuilt
        ###Above code we can apply anywhere it is fixed sir......

    return render(request,'blog/post_list1.html',{'post_list':post_list,'tag':tag})

from blog.forms import CommentForm
def post_detail_view(request,year,month,day,post):
    post = get_object_or_404(Post,slug=post,status='Published',publish__year=year,
                             publish__month=month,
                             publish__day=day)
    #now to implement comment we will use related name means post.comments (comment related to this post)
    comments=post.comments.filter(active=True)#i got all comment related to post.
    csubmit=False
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            csubmit=True

    else:
        #if not POST then we need to display form.:)
        form=CommentForm()
            ###lets visualize above 3 lines user will submit only 3 field data (name email and body but for which post that we are associating here.)
    return render(request,'blog/post_detail.html',{'post': post,'form':form,'csubmit':csubmit,'comments':comments})


######Mail functionality########
from django.core.mail import send_mail
from blog.forms import EmailSendForm
def mail_send_view(request,id):
    post=get_object_or_404(Post,id=id,status='Published')
    sent=False
    if request.method=='POST':
        # Now with that post data create form object.
        form=EmailSendForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='{}({}) recommends you to read "{}"'.format(cd['name'],cd['email'],post.title)
            post_url = request.build_absolute_uri(post.get_absolute_url())
            message="Please Read Post At:\n{}\n\n's Comments:\n{}".format(post_url,cd['name'],cd['comments'])
            # now cd will hve all end user provided data in dictionary form.:)
            send_mail(subject,message,'sry7771@gmail.com',[cd['to']])
            sent=True
    else:
        form = EmailSendForm()
        # create form object
    return render(request, 'blog/sharebymail.html', {'form': form, 'post': post,'sent':sent})








