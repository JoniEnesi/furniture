# Generated by Django 4.2.1 on 2023-06-08 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joniApp', '0003_rename_testimunial_image_testimonial_testimonial_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_descriptions',
            field=models.TextField(blank=True, max_length=700, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_legs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_pillows',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]