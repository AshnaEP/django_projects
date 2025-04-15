from django.contrib import admin
from cart.models import Cart,OrderDetails,Payment

# Register your models here.
admin.site.register(Cart)
admin.site.register(OrderDetails)
admin.site.register(Payment)
