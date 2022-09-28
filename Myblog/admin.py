from django.contrib import admin

# Register your models here.
from .models import Author, Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","content","comments","date")
    search_fields = ["title","content"]

admin.site.register(Article,ArticleAdmin)
admin.site.register(Author)

