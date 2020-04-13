from django.db import models

PRODUCTS = (
        ("Select", "Select"),
        ("Masks", "Masks"),
        ("Ventilators", "Ventilators"),
        ("Medicines & medical equipments", "Medicines & medical equipments"),
        ("Rooms", "Rooms"),
        ("Beds", "Beds"),
        ("Food", "Food"),
)

# Create your models here.
class Retailer(models.Model):
    """Retailers enter the availability of their products"""
    company_name = models.CharField(max_length=255)
    product = models.CharField(max_length=80, choices=PRODUCTS, default='Select')
    quantity = models.IntegerField(default=1)
    lat = models.CharField(max_length=15, null=False, default="0")
    long = models.CharField(max_length=15, null=False, default="0")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "{} has {}. Quantity: {}".format(self.company_name, self.product, self.quantity)