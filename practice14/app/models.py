from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.name}"





class Post(models.Model):
    author_post = models.CharField(max_length=10000)
    title_post = models.CharField(max_length=10000)
    text_post = models.CharField(max_length=10000)
    likes_post = models.PositiveIntegerField()
    tags = models.ManyToManyField(Tag)
    

    def __str__(self):
        return f"{self.author_post} - {self.title_post} - {self.text_post} - {self.likes_post}"
    

