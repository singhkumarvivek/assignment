from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image_type', 'image')
        CHOICES = (
            ("", 'Please select type'),
            (0, 'JPG'), 
            (1, 'PNG'),
        )
        widgets = {
            'image_type': forms.Select(choices=CHOICES,attrs={'class': 'form-control'}),
        }

class PostSearchForm(PostForm):   
    def __init__(self, *args, **kwargs):
        super(PostSearchForm, self).__init__(*args, **kwargs) 
        self.fields['image_type'].required=False
    class Meta:
        model = Post
        exclude = ('image',)
        CHOICES = (
            ("", 'Please select type'),
            (0, 'JPG'), 
            (1, 'PNG'),
        )
        widgets = {
            'image_type': forms.Select(choices=CHOICES,attrs={'class': 'form-control'}),
        }