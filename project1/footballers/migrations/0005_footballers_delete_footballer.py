# Generated by Django 5.0.4 on 2024-05-02 15:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footballers', '0004_alter_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footballers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('country', models.CharField(max_length=100)),
                ('club', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='footballers/')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='footballers.category')),
            ],
            options={
                'db_table': 'footballers',
            },
        ),
        migrations.DeleteModel(
            name='Footballer',
        ),
    ]
