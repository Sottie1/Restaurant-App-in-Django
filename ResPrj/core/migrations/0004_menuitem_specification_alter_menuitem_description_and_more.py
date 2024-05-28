# Generated by Django 5.0.6 on 2024-05-27 18:55

import ckeditor_uploader.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_menuitem_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='specification',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='MenuImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='menu_sub_images')),
                ('date', models.DateField(auto_now_add=True)),
                ('menuItem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='m_images', to='core.menuitem')),
            ],
            options={
                'verbose_name_plural': 'Menu Sub Images',
            },
        ),
    ]