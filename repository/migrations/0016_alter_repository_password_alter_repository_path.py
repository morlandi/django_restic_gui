# Generated by Django 4.0.5 on 2022-06-08 12:56

from django.db import migrations, models
from encrypted_model_fields.fields import EncryptedCharField, encrypt_str


def encrypt_existing_passwords(apps, schema_editor):

    repository_type = apps.get_model('repository', 'Repository')
    for repo in repository_type.objects.all():
        repo.password = encrypt_str(repo.password)
        repo.save()


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0015_alter_repository_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='password',
            field=EncryptedCharField(verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='repository',
            name='path',
            field=models.CharField(blank=True, help_text='Enter either a local path or the connection string for remote backup repo, i.e.: "sftp:remote_backup:restic"', max_length=256),
        ),
        migrations.RunPython(encrypt_existing_passwords),
    ]
