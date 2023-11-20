from django.db import models

# Create your models here.
class Post(models.Model):
    author_post = models.CharField(max_length=255)
    title_post = models.CharField(max_length=255)
    text_post = models.CharField(max_length=255)
    likes_post = models.PositiveIntegerField()
    

    def __str__(self):
        return f"{self.author_post} - {self.title_post} - {self.text_post} - {self.likes_post}"