from django.db import models
from cusauth.models import User
from django.utils.timezone import now 
from material.models import Material

# Create your models here.

class GRN(models.Model):
    grn_no = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    time = models.DateTimeField(default = now)
    vendor_address = models.CharField(max_length=100000,default='')
    delivery_address = models.CharField(max_length=100000,default='')
    item_po = models.CharField(max_length=1000000,default='')
    billing = models.CharField(max_length=100000,default='')
    maindata =models.CharField(max_length=10000,default='')


class MIR(models.Model):
    mir_no = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    time = models.DateTimeField(default = now)
    vendor_address = models.CharField(max_length=100000,default='')
    delivery_address = models.CharField(max_length=100000,default='')
    item_grn= models.CharField(max_length=1000000,default='')
    billing = models.CharField(max_length=100000,default='')
    maindata =models.CharField(max_length=10000,default='')

class MaterialIssue(models.Model):
    issue_no = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    time = models.DateTimeField(default = now)
    item_issue = models.CharField(max_length=1000000,default='')
    remarks = models.CharField(max_length=1000,default='')

