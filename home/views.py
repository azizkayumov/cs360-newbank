from django.shortcuts import render

# Create your views here.
def index(request):
    user = request.user
    return render(request, 'home/index.html', {'user': user})

def cards(request):
    return render(request, 'home/index.html')

def card_detail(request, card_type):
    
    context = {
        'card_name': card_type,
    }
    return render(request, 'home/card_detail.html', context)