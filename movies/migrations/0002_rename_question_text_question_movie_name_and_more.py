# Generated by Django 4.1.3 on 2022-12-05 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='movie_name',
        ),
        migrations.AddField(
            model_name='question',
            name='movie_description',
            field=models.CharField(default='SOME STRING', max_length=300),
        ),
    ]
