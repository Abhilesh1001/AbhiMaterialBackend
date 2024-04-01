from django.contrib import admin
from .models import PaymentTovendor,AdvancePayment
# Register your models here.


@admin.register(PaymentTovendor)
class AdminPaymenttoVEndor(admin.ModelAdmin):
    list_display=['payment_no','miro_no','amount_debit','user','time','advance_adjust']

@admin.register(AdvancePayment)
class AdminAdvancePayment(admin.ModelAdmin):
    list_display=['advance_payment_no','po_no','amount_debit','user','time']


