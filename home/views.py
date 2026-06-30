from django.shortcuts import render
from django.http import HttpResponse

# 1. Ensure the index view is completely restored
def index(request):
    user = request.user
    return render(request, 'home/index.html', {'user': user})

# 2. Keep the original cards view
def cards(request):
    return render(request, 'home/index.html')

# 3. Add our robust card details view mapping to an inline string fallback
def card_detail(request, card_name):
    formatted_name = card_name.capitalize()
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Card Information Portal</title>
        <style>
            body {{ font-family: sans-serif; background-color: #0f172a; color: #f8fafc; padding: 3rem; text-align: center; }}
            .card {{ background: #1e293b; padding: 2rem; border-radius: 8px; display: inline-block; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
            h1 {{ color: #38bdf8; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Card: {formatted_name}</h1>
            <p>Welcome to your secure transaction history pipeline overview.</p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)

from django.http import HttpResponse

def format_usd_display(amount):
    val_str = str(round(amount, 2))
    if '.' in val_str:
        parts = val_str.split('.')
        if len(parts[1]) == 1:
            val_str += '0'
    return f"${val_str} USD"

def format_eur_display(amount):
    val_str = str(round(amount, 2))
    if '.' in val_str:
        parts = val_str.split('.')
        if len(parts[1]) == 1:
            val_str += '0'
    return f"€{val_str} EUR"

def currency_view(request):
    return HttpResponse("<h1>NewBank Currency Exchange Hub</h1><p>Simple fix works!</p>")