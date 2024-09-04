from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306241764',
        'name': 'Figo Favian Ragazo',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
# Create your views here.
