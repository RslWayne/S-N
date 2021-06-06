from django import forms
from .models import Comment
from .models import Profile


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user',]

