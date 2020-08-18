from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'text':'hello', 'number':'123'}
    return render(request, 'basic_app/index.html', context = context)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/rel_url.html')
