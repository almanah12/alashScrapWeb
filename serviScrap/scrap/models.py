from django.db import models
from django.template.defaultfilters import slugify


class Personal(models.Model):
    login = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    name_shop = models.CharField(max_length=30)
    id_partner = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Personal'

    def __str__(self):
        return self.login


class Goods(models.Model):
    name = models.CharField(max_length=50)
    vendor_code = models.CharField(max_length=25, unique=True)
    price = models.CharField(max_length=20)
    availability = models.CharField(max_length=30)
    seller = models.ForeignKey('Sellers', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Good'

    def __str__(self):
        return self.name


class Sellers(models.Model):
    name = models.CharField(max_length=50)

    # courses = models.ManyToManyField(Goods

    def __str__(self):
        return self.name








