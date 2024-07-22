from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.

class Author(models.Model):
    author_dp = models.ImageField(upload_to='author dp')
    author_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=500, null=True, blank=True, unique=True)


    def __str__(self):
        return self.author_name
    

class BlogCategory(models.Model):
    title = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=500, null=True, blank=True, unique=True)


    def __str__(self):
        return self.title
    


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Blog(models.Model):
    blog_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    blog_category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=250)
    blog_cover = models.ImageField(upload_to='Blog image/')
    blog_content = models.TextField()
    blog_image_one = models.ImageField(upload_to='Blog image/')
    blog_image_two = models.ImageField(upload_to='Blog image/')
    quotes = models.TextField()
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(max_length=500, null=True, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.blog_title} -- {self.blog_author}"

    

class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=55)
    email = models.EmailField(max_length=75)
    message = models.TextField()
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.user_name
    


class Newsletter(models.Model):
    pass



def create_slug(instance, new_slug=None):
    if isinstance(instance, Blog):
        slug = slugify(instance.blog_title)
    elif isinstance(instance, BlogCategory):
        slug = slugify(instance.title)
    elif isinstance(instance, Author):
        slug = slugify(instance.author_name)
    else:
        return None

    if new_slug is not None:
        slug = new_slug
    
    ModelClass = instance.__class__
    qs = ModelClass.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = f"{slug}-{qs.first().id}"
        return create_slug(instance, new_slug=new_slug)
    return slug

@receiver(pre_save, sender=Blog)
@receiver(pre_save, sender=BlogCategory)
@receiver(pre_save, sender=Author)
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


# def create_slug(instance, new_slug = None):
#     slug = slugify(instance.Title)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Blog.objects.filter(slug = slug).order_by('-id')
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" %(slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug




# def pre_save_post_reciever(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)
# pre_save.connect (pre_save_post_reciever, Blog)
