from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name","email","comment")
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control col-sm-12"}),
            "email":forms.TextInput(attrs={"class":"form-control col-sm-12"}),
            "comment":forms.Textarea(attrs={"class":"form-control col-sm-12"})
        }