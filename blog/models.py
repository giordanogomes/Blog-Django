from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    titulo = models.CharField(max_length=255) # Título do post
    slug = models.SlugField(max_length=255, unique=True)
    # www.meusite.com.br/blog/introducao-ao-django <- slug
    autor = models.ForeignKey(User, on_delete=models.CASCADE)  # Autor do post
    body = models.TextField()  # Texto do post / corpo do post
    created = models.DateTimeField(auto_now_add=True)  # Add automaticamente a Data/Hora da criação do post
    updated = models.DateTimeField(auto_now=True)  # A cada modificação no post, atualiza automaticamente o campo updated

    class Meta:
        ordering = ("-created",)

    def __str__(self):  # Formatando título do Post
        return self.titulo

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})

