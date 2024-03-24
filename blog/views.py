from django.shortcuts import render
from django.views import generic
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from .models import Pattern

# Create your views here.

class PatternList(generic.ListView):
    queryset = Pattern.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6




def pattern_details(request, slug):
    queryset = Pattern.objects.filter(status=1)
    pattern = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/pattern_details.html",
        {
            "pattern": pattern,
          
        },
    )
