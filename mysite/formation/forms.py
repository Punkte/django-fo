from django import forms
from .models import Post , Contact

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('contact_object', 'content')