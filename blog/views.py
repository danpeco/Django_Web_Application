from django.shortcuts import render

posts = [
    {
        'author': 'DanielPC',
        'title': 'Blog post 1',
        'content': 'Content of first post',
        'date_posted': 'today'
    },
    {
        'author': 'Julio',
        'title': 'Blog post 2',
        'content': 'Content of second post',
        'date_posted': 'tomorrow'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

