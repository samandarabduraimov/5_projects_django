# Generated by Django 5.0.4 on 2024-05-02 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footballers', '0002_footballer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footballer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='footballers'),
        ),
    ]