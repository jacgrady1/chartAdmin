from django.shortcuts import render

# Create your views here.

def home(request):
    html='linePlusBarChart.html'
    return render(request, html)
