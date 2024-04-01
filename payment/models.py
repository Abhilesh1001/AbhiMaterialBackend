from django.db import models
from material.models import PurchaseOrder
from goodreceipt.models import MIR
from cusauth.models import User
from django.utils.timezone import now 
# Create your models here.

class AdvancePayment(models.Model):
    advance_payment_no = models.AutoField(primary_key=True)
    po_no = models.ForeignKey(PurchaseOrder,on_delete=models.CASCADE)
    amount_debit = models.DecimalField(max_digits=10, decimal_places=3)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    time = models.DateTimeField(default = now)



class PaymentTovendor(models.Model):
    payment_no = models.AutoField(primary_key=True)
    miro_no =  models.ForeignKey(MIR,on_delete=models.CASCADE)
    amount_debit = models.DecimalField(max_digits=10, decimal_places=3,default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    advance_adjust = models.DecimalField(max_digits=10, decimal_places=3,default=0)
    time = models.DateTimeField(default = now)




