from django.shortcuts import render

def main(request):
    return render(request, 'home/main.html')

def price(request):
    return render(request, 'home/price.html')

def about(request):
    return render(request, 'home/about.html')
