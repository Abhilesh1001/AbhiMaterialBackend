from django.contrib import admin
from . models import GRN,MIR,MaterialIssue

# Register your models here.
@admin.register(GRN)
class AdminGRN(admin.ModelAdmin):
    list_display = ['grn_no','item_po','user','time','vendor_address','delivery_address','maindata','billing',]

@admin.register(MIR)
class AdminMIR(admin.ModelAdmin):
    list_display = ['mir_no','user','time','vendor_address','delivery_address','item_grn','billing','maindata']

@admin.register(MaterialIssue)
class AdminMaterialIssue(admin.ModelAdmin):
    list_display = ['issue_no','user','time','item_issue']
