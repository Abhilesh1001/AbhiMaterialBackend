from django.db import models
from cusauth.models import User
from django.utils.timezone import now 

# Create your models here.

class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    email =models.EmailField(max_length=50)
    usersf = models.ForeignKey(User,on_delete=models.CASCADE)
    pan_no =  models.CharField(max_length=50)
    phone_no = models.CharField(max_length=15)
    time = models.DateTimeField(default = now)
    


# share holder fund 

class ShareHolder(models.Model):
    shf_id= models.AutoField(primary_key=True)
    person=models.ForeignKey(Person,on_delete=models.CASCADE)
    time = models.DateTimeField(default = now)
    uusersf = models.ForeignKey(User,on_delete=models.CASCADE)
    amount_credit =  models.DecimalField(max_digits=10, decimal_places=3)
    amount_Debit=  models.DecimalField(max_digits=10, decimal_places=3)
    collection_date = models.DateTimeField(blank=True, null=True)
    particulars =  models.CharField(max_length=100)


# RD collection 
    
class RDInt(models.Model):
    rd_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    usersf = models.ForeignKey(User,on_delete=models.CASCADE)
    time = models.DateTimeField(default = now)
    start_date = models.DateTimeField(blank=True, null=True)
    closing_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField() 
    duration = models.IntegerField()
    interest_rate =  models.IntegerField()



class RDColl(models.Model):
    rd_collection_id = models.AutoField(primary_key=True)
    rd_interest = models.ForeignKey(RDInt, on_delete=models.CASCADE)
    usersf = models.ForeignKey(User, on_delete=models.CASCADE)
    collection_date = models.DateTimeField(blank=True, null=True)
    time = models.DateTimeField(default = now)
    amount_collected = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)


# Loan 
    
class LoanInt(models.Model):
    loan_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person,on_delete= models.CASCADE)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    usersf = models.ForeignKey(User,on_delete=models.CASCADE)
    remarks = models.TextField(blank=True, null=True)
    is_active = models.BooleanField()
    time = models.DateTimeField(default = now)
    start_date = models.DateTimeField(blank=True, null=True)
    days = models.IntegerField()
    duration = models.IntegerField()
    closing_date = models.DateTimeField(blank=True, null=True)
    interest_rate =  models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.pk:  # This check ensures that it's a new loan (creation).
            self.opening_date = now()
        super().save(*args, **kwargs)


class LoanColl(models.Model):
    loan_collection_id = models.AutoField(primary_key=True)
    loan_intrest = models.ForeignKey(LoanInt, on_delete=models.CASCADE) 
    time =  models.DateTimeField(default = now)
    collection_date = models.DateTimeField(blank=True, null=True)
    amount_collected = models.DecimalField(max_digits=10, decimal_places=3)
    remarks = models.TextField(blank=True, null=True)
    usersf = models.ForeignKey(User,on_delete=models.CASCADE) 



class StaffSalary(models.Model):
    sd_id= models.AutoField(primary_key=True)
    person=models.ForeignKey(Person,on_delete=models.CASCADE)
    time = models.DateTimeField(default = now)
    usersf = models.ForeignKey(User,on_delete=models.CASCADE)
    amount_Debit =  models.DecimalField(max_digits=10, decimal_places=3)
    collection_date = models.DateTimeField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    
class Partuclars(models.Model):
    p_id = models.AutoField(primary_key=True)
    time = models.DateTimeField(default = now)
    usersf = models.ForeignKey(User,on_delete=models.CASCADE)
    amount_Debit =  models.DecimalField(max_digits=10, decimal_places=3)
    amount_credit = models.DecimalField(max_digits=10, decimal_places=3)
    particulars = models.TextField(blank=True, null=True)




class FixedDeposite(models.Model):
    fd_id= models.AutoField(primary_key=True)
    time = models.DateTimeField(default = now)
    usersf=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    amount_Debit =  models.DecimalField(max_digits=10, decimal_places=3,default=0)
    amount_credit = models.DecimalField(max_digits=10, decimal_places=3,default=0) 
    collection_date = models.DateTimeField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    closing_date = models.DateTimeField(blank=True, null=True)
    duration = models.DecimalField(max_digits=10, decimal_places=3,default=0)
    interest_rate =  models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    person=models.ForeignKey(Person,on_delete=models.CASCADE,default=1)

class Asset(models.Model):
    asset_no =models.AutoField(primary_key=True) 
    time = models.DateTimeField(default = now)
    asset_name = models.TextField(blank=True, null=True,default='')
    usersf=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    amount_Debit =  models.DecimalField(max_digits=10, decimal_places=3,default=0)
    debit_date = models.DateTimeField(blank=True, null=True)






