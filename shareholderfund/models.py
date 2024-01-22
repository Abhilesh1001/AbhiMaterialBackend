from django.db import models
from cusauth.models import User
from django.utils.timezone import now 
from django.utils import timezone
# Create your models here.

class ShareHolderName(models.Model):
    Sh_id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    email =models.EmailField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pan_no =  models.CharField(max_length=50)
    phone_no = models.CharField(max_length=15)
    time = models.DateTimeField(default = now)


class ShareHolderFuns(models.Model):
    shf_id= models.AutoField(primary_key=True)
    sh_name=models.ForeignKey(ShareHolderName,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount_credit =  models.FloatField(null=True, blank=True)
    amount_Debit=  models.FloatField(null=True, blank=True)
    time = models.DateTimeField(default = now)
    particulars =  models.CharField(max_length=100)




class RdPerson(models.Model):
    rdp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)



class RDCollection(models.Model):
    person = models.ForeignKey(RdPerson, on_delete=models.CASCADE)
    collection_date = models.DateField(default = now)
    amount_collected = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField(blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


