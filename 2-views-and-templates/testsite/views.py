from django.shortcuts import render

def home(request, name):
    context = {
        'name': name,
        'langs': ['JavaScript', 'Python', 'Java', 'Go', 'C++']
    }
    return render(
        request,
        'home.html',
        context
    )