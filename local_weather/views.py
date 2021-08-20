from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'value1': 5, 'value2': 10};
    return render(request, 'local_weather/index.html', context)
