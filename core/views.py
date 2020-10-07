from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, num1, num2):
    soma = num1 + num2
    return HttpResponse('A soma é {}'.format(soma))
