from django.shortcuts import render
#from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class BlogView(ListView):#this is to view content in list
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):#single content
    model = Post
    template_name = "post_details.html"

class CreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields='__all__'

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields=['title','body','img']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('BlogView')