from django.db import models

# Create your models here.

class Author(models.Model):
    author_dp = models.ImageField(upload_to='author dp')
    author_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BlogCategory(models.Model):
    title = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Blog (models.Model):
    blog_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    blog_category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=250)
    blog_cover = models.ImageField(upload_to='Blog image/')
    blog_content = models.TextField()
    blog_image_one = models.ImageField(upload_to='Blog image/')
    blog_image_two = models.ImageField(upload_to='Blog image/')
    quotes = models.TextField()
    tags = models.ManyToManyField(Tag)

class Comment(models.Model):
    user_name = models.CharField(max_length=55)
    email = models.EmailField(max_length=75)
    message = models.TextField()

    def __str__(self):
        return self.user_name
    


class Newsletter(models.Model):
    pass