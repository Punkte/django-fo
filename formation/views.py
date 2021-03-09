from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Contact
from django.utils import timezone
from django.shortcuts import render
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, ContactForm
from django.shortcuts import redirect
import json

# Create your views here.
def index(request):
    return render(request, 'formation/index.html')

def blog(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contact/contact_detail.html', {'contact': contact})

def contact_new(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.published_date = timezone.now()
            contact.status = 'UR'
            contact.save()
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ContactForm()
    return render(request, 'contact/index.html', {'form': form})