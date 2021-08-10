# Generated by Django 3.1.7 on 2021-04-20 09:09

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructionapp', '0010_subserviceslist'),
    ]

    operations = [
        migrations.AddField(
            model_name='subserviceslist',
            name='service_title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='subserviceslist',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
