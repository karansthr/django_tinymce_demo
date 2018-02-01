from django import forms
from .models import Post
from tinymce import TinyMCE


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCE(attrs={
            'required': False,
            'cols': 30,
            'rows': 10
        }))

    class Meta:
        model = Post
        fields = '__all__'
