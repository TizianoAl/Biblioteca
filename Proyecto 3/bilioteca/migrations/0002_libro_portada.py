# Generated by Django 2.2 on 2020-08-19 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bilioteca', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='portada',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
