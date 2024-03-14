from django.contrib import admin
from .models import ShareHolderName,ShareHolderFuns,RDCollection,RdPerson,LoanCollection,LoanPerson,LoanAmount,RDCollectionNew,RDIntrest

# Register your models here.

@admin.register(ShareHolderName)
class AdminShareHolderName(admin.ModelAdmin):
    list_display = ['Sh_id','name','email','user','pan_no','time']

@admin.register(ShareHolderFuns)
class AdminSShareHolderFuns(admin.ModelAdmin):
    list_display = ['shf_id','sh_name','user','amount_credit','amount_Debit','time','particulars']


@admin.register(RDCollection)
class AdminRDCollection(admin.ModelAdmin):
    list_display = ['id','person','amount_collected','remarks','user','collection_date']

@admin.register(RdPerson)
class AdminRDPerson(admin.ModelAdmin):
    list_display = ['rdp_id','name','user','email','phone_no','time']


@admin.register(LoanCollection)
class AdminLoanCollection(admin.ModelAdmin):
    list_display = ['id','loan_person','amount_collected','remarks','user','collection_date']
    

@admin.register(LoanPerson)
class AdminLoanPerson(admin.ModelAdmin):
    list_display = ['loan_id','name','user','email','phone_no','time']

@admin.register(LoanAmount)
class AdminLoanAmount(admin.ModelAdmin):
    list_display = ['id' ,'loan_person','loan_amount','remarks','is_active','time','opening_date','closing_date']

@admin.register(RDIntrest)
class AdminRdintrest(admin.ModelAdmin):
    list_display = ['rd_intrest_id','person','start_date','closing_date','is_active','duration','interest_rate']
    
@admin.register(RDCollectionNew)
class AdminRdcollectionNew(admin.ModelAdmin):
    list_display = ['rd_intrest','collection_date','amount_collected','remarks','user']




