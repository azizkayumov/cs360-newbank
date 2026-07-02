from django.shortcuts import render
from django.shortcuts import redirect
from accounts.models import Account
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponse

# Create your views here.
def my_account(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    return render(request, 'accounts/my_account.html', {'account': request.user})

def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:my_account')
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('accounts:my_account')
        error_message = 'Invalid username or password'
    return render(request, 'accounts/login.html', {'error_message': error_message})

def lookup(request):
    username = request.GET.get('username', '')
    query = "SELECT * FROM accounts_account WHERE username = '" + username + "'"
    accounts = Account.objects.raw(query)
    results = "<br>".join(account.username for account in accounts) or "No matching accounts."
    return HttpResponse(f"<h2>Account lookup</h2><p>Query: {query}</p><p>Results: {results}</p>")


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

def register(request):
    if request.user.is_authenticated:
        return redirect('accounts:my_account')
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if Account.objects.filter(username=username).exists():
            #error_message = 'Username already exists'
            error_message = 'Invalid credentials'
        elif Account.objects.filter(email=email).exists():
            #error_message = 'Email already exists'
            error_message = 'Invalid credentials'
        else:
            account = Account.objects.create_user(username=username, password=password, email=email, balance=100.00)
            auth_login(request, account)
            return redirect('accounts:my_account')
    return render(request, 'accounts/register.html', {'error_message': error_message})