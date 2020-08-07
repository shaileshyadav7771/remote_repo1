from django import forms
class EmailSendForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=True, widget=forms.Textarea)
    #here comment is not manadatory so we are taking required=False and comment can be of any size that is why we are taking text ared.

from blog.models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','body')



