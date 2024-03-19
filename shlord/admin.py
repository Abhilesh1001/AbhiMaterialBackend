from django.contrib import admin
from .models import Person,LoanInt,LoanColl,ShareHolder,RDColl,RDInt

# Register your models here.


@admin.register(Person)
class AdminShareHolderName(admin.ModelAdmin):
    list_display = ['person_id','name','email','pan_no','time']

@admin.register(ShareHolder)
class AdminSShareHolderFuns(admin.ModelAdmin):
    list_display = ['shf_id','person','time','amount_credit','amount_Debit','collection_date','particulars']

@admin.register(RDInt)
class AdminRdintrest(admin.ModelAdmin):
    list_display = ['rd_id','person','time','start_date','closing_date','is_active','duration','interest_rate']


@admin.register(RDColl)
class AdminRdcollection(admin.ModelAdmin):
    list_display = ['rd_collection_id','rd_interest','collection_date','time','amount_collected','remarks']


@admin.register(LoanInt)
class AdminLoanAmount(admin.ModelAdmin): 
    list_display = ['loan_id' ,'person', 'loan_amount', 'remarks','is_active','time','start_date','days','duration','closing_date','interest_rate']


@admin.register(LoanColl)
class AdminLoanCollection(admin.ModelAdmin):
    list_display = ['loan_collection_id','loan_intrest','time','collection_date','amount_collected','remarks']



