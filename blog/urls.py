from django.urls import path
from . import views

app_name = "blog"  # referencia as urls do arquivo


urlpatterns = [   # lista de padrões de urls
    path("", views.PostListView.as_view(), name="list"),  # irá acessar a lista de posts
    path("<slug:slug>/", views.PostDetailView.as_view(), name="detail"),  # irá acessar página do post
]



