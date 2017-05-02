from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def exhibits(request):
    return render(request, 'home.html')


def learn(request):
    return render(request, 'home.html')


def visit(request):
    return render(request, 'visit.html')


def about(request):
    return render(request, 'home.html')


def faq(request):
    return render(request, 'faq.html')


def resources(request):
    return render(request, 'resources.html')
