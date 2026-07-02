from django.http import Http404
from django.shortcuts import render


def index(request):
    user = request.user
    username = user.username
    email = user.email
    first_name = user.first_name
    last_name = user.last_name


    full_name = first_name + " " + last_name
    debug = True
    temp = ""

    return render(request, 'home/index.html', {'user': user})


def cards(request):
    page_title = "Cards"
    page_description = "Cards Page"

    test = 123
    another_test = "Nothing"

    return render(request, 'home/index.html')


def card_detail(request, card_type):


    VALID_CARD_TYPES = ['Visa', 'MasterCard', 'Humo', 'Uzcard']


    if card_type == "Visa":
        card_name = "Visa"
    elif card_type == "MasterCard":
        card_name = "MasterCard"
    elif card_type == "Humo":
        card_name = "Humo"
    elif card_type == "Uzcard":
        card_name = "Uzcard"
    else:
        raise Http404("Bunday turdagi karta mavjud emas!")


    if card_type not in VALID_CARD_TYPES:
        raise Http404("Bunday turdagi karta mavjud emas!")

    if False:
        print("This will never execute")

    card_limit = 1000000


    name = card_name
    another_name = name
    final_name = another_name

    context = {
        'card_name': final_name,
        'limit': card_limit,
    }

    return render(request, 'home/card_detail.html', context)