# Generated by Django 3.2.4 on 2021-07-03 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructionapp', '0019_auto_20210703_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfoliostatus',
            name='portfolio',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='status',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='constructionapp.portfoliostatus'),
            preserve_default=False,
        ),
    ]
