# Generated by Django 5.0.3 on 2024-03-21 09:01

import django_summernote.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_alter_about_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='services/')),
                ('description', django_summernote.fields.SummernoteTextField()),
            ],
        ),
    ]
