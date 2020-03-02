from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

def all_products(request):
    products = Product.objects.all() # returns all the products in the db.
    return render(request, "products.html", {"products":products})
      