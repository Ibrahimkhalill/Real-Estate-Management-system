from django.contrib import admin

# Register your models here.
from mainapp.models import *

admin.site.register(Company)
admin.site.register(Broker)
admin.site.register(Properties)
admin.site.register(Sold)
admin.site.register(Seller)