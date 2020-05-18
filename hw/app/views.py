from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    num_movie_posts = Post.objects.filter(category='movie').count()
    num_drama_posts = Post.objects.filter(category='drama').count()
    num_entertain_posts = Post.objects.filter(category='entertain').count()
    return render(request, 'index.html', {
        'num_movie_posts':num_movie_posts, 
        'num_drama_posts': num_drama_posts, 
        'num_entertain_posts': num_entertain_posts
    })

def movie(request):
    movie_posts = Post.objects.filter(category = 'movie')
    return render(request, 'movie.html', {'movie_posts': movie_posts})

def drama(request):
    drama_posts = Post.objects.filter(category = 'drama')
    return render(request, 'drama.html', {'drama_posts': drama_posts})

def entertain(request):
    entertain_posts = Post.objects.filter(category = 'entertain')
    return render(request, 'entertain.html', {'entertain_posts': entertain_posts})


def detail(request, pk_i_clicked):
    article = Post.objects.get(pk=pk_i_clicked)
    return render(request, 'detail.html', {'an_article_i_will_use_in_html':article})

def new(request):
    if request.method == 'POST':
        print(request.POST)
        new_article = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category']
        )
        return redirect('detail', pk_i_clicked = new_article.pk)
    
    else:
        return render(request, 'new.html')
