# Generated by Django 4.0.5 on 2022-06-13 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main',
            name='main_img',
        ),
    ]