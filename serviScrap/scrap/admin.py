from django.contrib import admin
from .models import Goods, Personal, Sellers

admin.site.register(Personal)
admin.site.register(Sellers)
admin.site.register(Goods)
