from django.db import models
from cusauth.models import User
from django.utils.timezone import now 


# Create your models here.
class Material(models.Model):
    s_no = models.AutoField(primary_key=True)
    material_name = models.CharField(max_length=100)
    material_group = models.CharField(max_length=40)
    unit = models.CharField(max_length=20)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    time = models.DateTimeField(default = now)



#Absoulte 
class PurchaseRequest(models.Model):
    s_no = models.AutoField(primary_key=True)
    material = models.ForeignKey(Material,on_delete=models.CASCADE)
    materia_price = models.IntegerField(default=0)
    material_qty = models.IntegerField(default=0)
    material_text = models.CharField(max_length=5000,default='')
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    time = models.DateTimeField(default = now)
    item_json = models.CharField(max_length=100000,default='')


class Vendor(models.Model):
    s_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    vendor_name = models.CharField(max_length=100)
    gst = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

class PurchaseRequestNew(models.Model):
    pr_no = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    time = models.DateTimeField(default = now)
    item_json = models.CharField(max_length=100000,default='')


class DeliveryAdress(models.Model):
    s_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    vendor_name = models.CharField(max_length=100)
    gst = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=100)


class PurchaseOrder(models.Model):
    po_no = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    time = models.DateTimeField(default = now)
    item_pr = models.CharField(max_length=1000000,default='')
    vendor_address = models.CharField(max_length=100000,default='')
    delivery_address = models.CharField(max_length=100000,default='')
    maindata = models.CharField(max_length=10000,default='')
