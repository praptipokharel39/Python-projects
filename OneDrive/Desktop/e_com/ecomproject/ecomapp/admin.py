from django.contrib import admin
from .models import *

admin.site.register([Customer,Category,Product,Cart,CartProducts,Order])

# Register your models here.
