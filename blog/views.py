from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Posting

class BlogListView(ListView):
    model = Posting
    template_name = "home.html"

class BlogDetailView(DetailView):
    model = Posting
    template_name = "post_detail.html"

