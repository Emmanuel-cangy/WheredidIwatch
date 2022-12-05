# Generated by Django 4.1.3 on 2022-12-05 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(blank=True, default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=200)),
                ('movie_description', models.CharField(default='', max_length=300)),
                ('watched_date', models.DateTimeField(verbose_name='date watched')),
                ('provider222', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.choice')),
            ],
        ),
    ]
