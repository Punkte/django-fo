from django import forms
from .models import Post , Contact, CV, Skill

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('contact_object', 'content')

class CvForm(forms.ModelForm):

    class Meta:
        model = CV
        fields = ['name', 'first_name', 'description', 'skills']
    name = forms.CharField()
    first_name = forms.CharField()
    description = forms.CharField()
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
        # fields = ('name', 'first_name', 'description', 'skills')
        