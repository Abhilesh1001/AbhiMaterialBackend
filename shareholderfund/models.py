from django.db import models
from cusauth.models import User
from django.utils.timezone import now 

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
    email =models.EmailField(max_length=50,default='')
    pan_no =  models.CharField(max_length=50,default='')
    phone_no = models.CharField(max_length=15,default='')
    time = models.DateTimeField(default = now)



class RDCollection(models.Model):
    person = models.ForeignKey(RdPerson, on_delete=models.CASCADE)
    collection_date = models.DateTimeField(default = now)
    amount_collected = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


class LoanPerson(models.Model):
    loan_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email =models.EmailField(max_length=50,default='')
    pan_no =  models.CharField(max_length=50,default='')
    phone_no = models.CharField(max_length=15,default='')
    time = models.DateTimeField(default = now)



class LoanCollection(models.Model):
    loan_person = models.ForeignKey(LoanPerson, on_delete=models.CASCADE)
    collection_date = models.DateTimeField(default = now)
    amount_collected = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    


class LoanAmount(models.Model):
    loan_person = models.ForeignKey(LoanPerson,on_delete= models.CASCADE)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    remarks = models.TextField(blank=True, null=True)
    is_active = models.BooleanField()
    time = models.DateTimeField(default = now)
    opening_date = models.DateTimeField(default=now)
    start_date = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(default=0)
    closing_date = models.DateTimeField(blank=True, null=True)
    interest_rate =  models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.pk:  # This check ensures that it's a new loan (creation).
            self.opening_date = now()
        super().save(*args, **kwargs)
    



class RDIntrest(models.Model):
    rd_intrest_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(RdPerson, on_delete=models.CASCADE)
    start_date = models.DateTimeField(blank=True, null=True)
    closing_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField() 
    duration = models.IntegerField()
    interest_rate =  models.IntegerField()


class RDCollectionNew(models.Model):
    rd_intrest = models.ForeignKey(RDIntrest, on_delete=models.CASCADE, default=None)
    collection_date = models.DateTimeField(default=now)
    amount_collected = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


 
class LoanCollectionNew(models.Model): 
    loan_intrest = models.ForeignKey(LoanAmount, on_delete=models.CASCADE) 
    collection_date = models.DateTimeField(default = now)
    amount_collected = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
