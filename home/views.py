from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse

# 1. Ensure the index view is completely restored
def index(request):
    user = request.user
    return render(request, 'home/index.html', {'user': user})

# 2. Keep the original cards view
def cards(request):
    return render(request, 'home/index.html')

def card_detail(request, card_type):
    # Ruxsat etilgan kartalar ro'yxati
    VALID_CARD_TYPES = ['Visa', 'MasterCard', 'Humo', 'Uzcard']
    
    # Kiritilgan qiymatni ro'yxatdagilar bilan solishtirish (registrni hisobga olmaslik ham mumkin, masalan .title() bilan)
    # Biz aniq moslikni tekshiramiz:
    if card_type not in VALID_CARD_TYPES:
        raise Http404("Bunday turdagi karta mavjud emas!")

    context = {
        'card_name': card_type,
    }
    return render(request, 'home/card_detail.html', context)
