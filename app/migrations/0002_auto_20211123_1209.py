# Generated by Django 3.2.9 on 2021-11-23 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=35)),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='imagespin',
            name='slug',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='imagespin',
            name='tags',
        ),
        migrations.AddField(
            model_name='imagespin',
            name='tags',
            field=models.ManyToManyField(related_name='photos', to='app.Tag'),
        ),
    ]
