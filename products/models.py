from django.db import models

# Create your models here.

 
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    thumbnail = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=100, null=True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Product, self).save(*args, **kwargs)
     
class product_images(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE,verbose_name = "Product",related_name="Image")
    image = models.ImageField(upload_to='products/')
    image_description = models.TextField()
    active = models.BooleanField(default=False)
    def __str__(self):
        return(self.product.name)