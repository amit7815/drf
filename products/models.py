from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=99.99)

    @property 
    def sale_price(self):    # this we can access by Product.objects.last().sale_price now we can user sale_price as a attribute of model
        return "%0.2f" %(float(self.price) * 0.8)

    def get_discount(self):
        return "122"