from django import forms

from .models import Comment, Post, User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email'
        ]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
