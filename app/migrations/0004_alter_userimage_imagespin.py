# Generated by Django 3.2.9 on 2021-11-29 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_folder_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='imagesPin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pin_images', to='app.imagespin'),
        ),
    ]
