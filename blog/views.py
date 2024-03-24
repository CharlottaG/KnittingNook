from django.shortcuts import render
from django.views import generic
from .models import Pattern

# Create your views here.

class PatternList(generic.ListView):
    queryset = Pattern.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6