# Generated by Django 3.1.2 on 2020-10-23 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('repository', '0005_auto_20201023_1015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fileext',
            options={'verbose_name': 'File extension', 'verbose_name_plural': 'File extensions'},
        ),
        migrations.AlterModelOptions(
            name='filetype',
            options={'verbose_name': 'File type', 'verbose_name_plural': 'File types'},
        ),
        migrations.AlterField(
            model_name='fileext',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='fileext',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.filetype', verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='filetype',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='filetype',
            name='svg_path',
            field=models.CharField(max_length=500, verbose_name='SVG Path'),
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')),
                ('action', models.CharField(max_length=50, verbose_name='Action')),
                ('path', models.CharField(max_length=200, verbose_name='Path')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Journal',
            },
        ),
    ]
