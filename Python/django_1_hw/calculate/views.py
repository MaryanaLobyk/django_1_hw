from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home/home.html')


def calculate(request, x, y, operation):
    result = 0
    if operation == '+':
        result = f'{x} + {y} = {x + y}'
    elif operation == '-':
        result = f'{x} - {y} = {x - y}'
    elif operation == '*':
        result = f'{x} * {y} = {x * y}'
    elif operation == 'div':
        result = f'{x} / {y} = {x / y}'
    else:
        result = 'ERROR'
    return render(request, 'calc/calc.html', {'result': result})
