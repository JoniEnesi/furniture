# Generated by Django 4.2.1 on 2023-06-08 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joniApp', '0002_testimonial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonial',
            old_name='testimunial_image',
            new_name='testimonial_image',
        ),
    ]
