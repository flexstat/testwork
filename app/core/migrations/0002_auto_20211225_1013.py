# Generated by Django 3.0.7 on 2021-12-25 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Статью', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AddField(
            model_name='articles',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор статьи'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
    ]