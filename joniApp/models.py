from django.db import models

# Create your models here.

class Color(models.Model):
    color_id = models.AutoField(primary_key=True)
    color_name = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return f'{self.color_name}'


class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    material_name = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return f'{self.material_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=60, null=True, blank=True)
    category_image = models.ImageField(upload_to='product/')

    def __str__(self):
        return f'{self.category_name}'

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=60, null=True, blank=True)
    product_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    product_review = models.TextField(max_length=500, null=True, blank=True)
    product_descriptions = models.TextField(max_length=700, null=True, blank=True)
    product_legs = models.IntegerField(null=True, blank=True)
    product_pillows = models.IntegerField(null=True, blank=True)
    product_image = models.ImageField(upload_to='product/')
    product_color = models.ManyToManyField(Color)
    product_material = models.ManyToManyField(Material)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.product_name}'

class Testimonial(models.Model):
    testimonial_image = models.ImageField(upload_to='testimonial/')
    testimonial_id = models.AutoField(primary_key=True)
    testimonial_description = models.TextField(max_length=500, null=True, blank=True)
    testimonial_author = models.CharField(max_length=60, null=True, blank=True)
    testimonial_post = models.CharField(max_length=60, null=True, blank=True)
    testimonial_review = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.testimonial_id}'


class Cotact(models.Model):
    contact_name = models.CharField(max_length=60, null=True, blank=True)
    contact_surname = models.CharField(max_length=60, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_comment = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.contact_name} {self.contact_surname}'