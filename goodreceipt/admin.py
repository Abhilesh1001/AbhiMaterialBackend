from django.contrib import admin
from . models import GRN

# Register your models here.
@admin.register(GRN)
class AdminGRN(admin.ModelAdmin):
    list_display = ['grn_no','item_po','user','time','vendor_address','delivery_address','maindata','billing',]

