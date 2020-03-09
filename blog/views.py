from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponse

# Create your views here.
# posts = [
#     {
#         'author': 'Mostafizur',
#         'title': 'Django is the best for framework lover',
#         'description': 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source.',
#         'postdate': '19 Dec 2019'
#     },

#     {
#         'author': 'Mostafizur',
#         'title': 'Laravel is the second best for framework lover',
#         'description': 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source.',
#         'postdate': '19 Dec 2019'
#     }
# ]

def home(request):
    posts = Post.objects.all()
    context = {
        'title' : 'Home page',
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)
    #return HttpResponse('<h2>Home Page</h2>')


def about(request):
    return render(request, 'blog/about.html', { 'title': 'About page'})


#CRUD
#create, retrieve, update, delete

def post_details(request, slug):
    upost = get_object_or_404(Post, slug=slug)
    context = {
        'title' : upost.title,
        'post' : upost
    }
    return render(request, 'blog/single_post.html', context)



#my cutom python, django code debug

# import os

# # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# VENV_PATH = os.path.dirname(BASE_DIR)

# STATIC_ROOT = os.path.join(VENV_PATH, 'static_root')
# # abs = os.path.dirname(os.path.abspath(__file__))

# Another test for rndom string

# import random
# import string

# def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))



#def mydebug(request):
    #result = 'My debug page'
    #return HttpResponse('No test now :)')
    # return HttpResponse(STATIC_ROOT)
    #return HttpResponse(random_string_generator(size=50))
    
    
    # print(random_string_generator())
    # print(random_string_generator(size=50))


