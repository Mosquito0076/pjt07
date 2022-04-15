from django.contrib import admin
from .models import Movie, Comment

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'user_id',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'movie_id', 'user_id',)


admin.site.register(Movie, MovieAdmin)
admin.site.register(Comment, CommentAdmin)