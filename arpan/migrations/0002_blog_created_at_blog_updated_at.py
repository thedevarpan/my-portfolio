# Generated by Django 5.0.7 on 2024-07-22 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arpan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
