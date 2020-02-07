from django.shortcuts import redirect

def redirectLogin(request):
    return redirect('login/')