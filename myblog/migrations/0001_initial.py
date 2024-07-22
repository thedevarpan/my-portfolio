# Generated by Django 5.0.7 on 2024-07-22 14:34

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_dp', models.ImageField(upload_to='author dp')),
                ('author_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=250)),
                ('blog_cover', models.ImageField(upload_to='Blog image/')),
                ('blog_content', models.TextField()),
                ('blog_image_one', models.ImageField(upload_to='Blog image/')),
                ('blog_image_two', models.ImageField(upload_to='Blog image/')),
                ('quotes', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('blog_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.author')),
                ('blog_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.blogcategory')),
                ('tags', models.ManyToManyField(to='myblog.tag')),
            ],
        ),
        migrations.CreateModel(
            name='AddComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('commentor_name', models.CharField(max_length=55)),
                ('commentor_email', models.EmailField(max_length=75)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.blog')),
            ],
        ),
    ]
