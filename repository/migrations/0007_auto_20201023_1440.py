# Generated by Django 3.1.2 on 2020-10-23 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0006_auto_20201023_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journal',
            name='path',
        ),
        migrations.AddField(
            model_name='journal',
            name='data',
            field=models.CharField(default='', max_length=200, verbose_name='Data'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='journal',
            name='action',
            field=models.CharField(choices=[('01', 'Backup'), ('02', 'Backup (new)'), ('03', 'Restore'), ('04', 'New Repository'), ('05', 'Repository changed')], max_length=2, verbose_name='Action'),
        ),
    ]
