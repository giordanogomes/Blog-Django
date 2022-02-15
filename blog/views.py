from django.views.generic import DetailView, ListView

# DetailView -> mostra somente 1 post
# ListView -> listar os posts

from .models import Post


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post

