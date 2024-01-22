from django.contrib import admin
from .models import ShareHolderName,ShareHolderFuns,RDCollection,RdPerson

# Register your models here.

@admin.register(ShareHolderName)
class AdminShareHolderName(admin.ModelAdmin):
    list_display = ['Sh_id','name','email','user','pan_no','time']

@admin.register(ShareHolderFuns)
class AdminSShareHolderFuns(admin.ModelAdmin):
    list_display = ['shf_id','sh_name','user','amount_credit','amount_Debit','time','particulars']


@admin.register(RDCollection)
class AdminRDCollection(admin.ModelAdmin):
    list_display = ['person','collection_date','amount_collected','remarks','user','collection_date']

@admin.register(RdPerson)
class AdminRdPerson(admin.ModelAdmin):
    list_display = ['rdp_id','name','user']

