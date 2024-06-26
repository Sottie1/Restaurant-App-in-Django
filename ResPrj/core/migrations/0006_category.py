# Generated by Django 5.0.6 on 2024-05-28 00:37

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_menuitem_menuimages_menuit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='category_Images/')),
                ('description', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
