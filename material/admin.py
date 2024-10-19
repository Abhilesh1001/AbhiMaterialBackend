from django.contrib import admin
from .models import Material,PurchaseRequest,Vendor,PurchaseRequestNew,DeliveryAdress,PurchaseOrder,MaterialGroup,MaterialUnit,StoreLocation,CompanyAddress

# Register your models here.

@admin.register(Material)
class AdminMaterial(admin.ModelAdmin):
    list_display = ['s_no','material_name','material_group','unit','user','time']


@admin.register(PurchaseRequest)
class AdminPurchaseRequest(admin.ModelAdmin):
    list_display=['s_no','material','materia_price','material_qty','material_text','user','time']

@admin.register(Vendor)
class AdminVendor(admin.ModelAdmin):
    list_display=['s_no','name','phone_no','vendor_name','gst','email','address']

@admin.register(PurchaseRequestNew)
class AdminPurchaseRequestNew(admin.ModelAdmin):
    list_display=['pr_no','user','time','item_json']

@admin.register(DeliveryAdress)
class AdminDeliveryAdress(admin.ModelAdmin):
    list_display=['s_no','name','phone_no','vendor_name','gst','email','address','company_address']

@admin.register(PurchaseOrder)
class AdminPurchaseOrder(admin.ModelAdmin):
    list_display=['po_no','user','time','item_pr','vendor_address','delivery_address','maindata']


@admin.register(MaterialGroup)
class AdminMaterilaGroup(admin.ModelAdmin):
    list_display=['group_no','group_name']

@admin.register(MaterialUnit)
class AdminMaterilaUnit(admin.ModelAdmin):
    list_display=['unit_no','material_umit','materil_unit_desc']


@admin.register(StoreLocation)
class AdminStoreLocation(admin.ModelAdmin):
    list_display=['store_no','store_id','store_description']

@admin.register(CompanyAddress)
class AdminCompanyAddress(admin.ModelAdmin):
    list_display=['s_no','name','address']

