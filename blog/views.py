from django.shortcuts import render
from django.views import generic
from .models import Pattern

# Create your views here.

class PatternList(generic.ListView):
    queryset = Pattern.objects.all()
    template_name = "pattern_list.html"