from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    user = request.user
    return render(request, 'home/index.html', {'user': user})

def cards(request):
    return render(request, 'home/index.html')


def search(request):
    search_term = request.GET.get('q', 'nothing')
    return HttpResponse(f"<h1>Search results</h1><p>You searched for: {search_term}</p>")