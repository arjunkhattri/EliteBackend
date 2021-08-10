# Generated by Django 3.1.7 on 2021-03-20 12:58

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=' ', max_length=254)),
                ('heading', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=' ', max_length=254)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=' ', max_length=254)),
                ('shortdesc', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('thumb', models.ImageField(upload_to='media/services')),
                ('aboutdesc', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=254, null=True)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('bg_image', models.ImageField(upload_to='media/Slider')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('designation', models.CharField(max_length=254)),
                ('profilepic', models.ImageField(upload_to='media/team')),
                ('Bio', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('address', models.CharField(max_length=254)),
                ('phone', models.FloatField(max_length=254)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('website', models.URLField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=254)),
                ('image', models.ImageField(upload_to='media/testimonialthumb')),
                ('quote', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.CreateModel(
            name='Preview_Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=' ', max_length=254, null=True)),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructionapp.services')),
            ],
        ),
    ]
