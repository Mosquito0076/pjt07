from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.title




class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)

    
    def __str__(self):
        return self.content