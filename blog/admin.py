from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "slug", "autor", "created", "updated",)
    prepopulated_fields = {"slug": ("titulo",)}


