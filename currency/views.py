
from django.http import HttpResponse
from django.db import connection
from .models import ExchangeHistory


def search_currency(request):
    code = request.GET.get('code', '')

    cursor = connection.cursor()

    query = f"SELECT * FROM currency_currency WHERE code = '{code}'"

    cursor.execute(query)

    result = cursor.fetchall()

    return HttpResponse(result)



def transaction_detail(request, id):
    transaction = ExchangeHistory.objects.get(id=id)

    return HttpResponse(
        f"{transaction.user} | "
        f"{transaction.from_currency} -> "
        f"{transaction.to_currency}"
    )