from django.db import models
from datetime import date

# Create your models here.
class Company(models.Model):
    company_name =models.CharField(max_length=55)
    company_prop_name =models.CharField(max_length=55)
    company_address_line1 =models.CharField(max_length=55)
    company_address_line2 =models.CharField(max_length=55)
    company_district =models.CharField(max_length=55)
    company_state =models.CharField(max_length=55)
    company_pin =models.CharField(max_length=6)
    company_primary_contact =models.CharField(max_length=10,unique=True)
    company_secondary_contact =models.CharField(max_length=10)
    company_email =models.EmailField(max_length=75)
    company_gstn =models.CharField(max_length=15)
    company_pan =models.CharField(max_length=10)
    company_bank_name =models.CharField(max_length=55)
    company_bank_address =models.CharField(max_length=55)
    company_bank_ifsc =models.CharField(max_length=15)
    company_bank_account_no =models.CharField(max_length=25)    
    company_logo =models.CharField(max_length=55)
    company_created_on =models.DateField()
    company_active =models.BooleanField(default=False) 
    
    def __self__(self):
        return f"{self.company_name}"


class Colors(models.Model):
    name = models.CharField(max_length=40)
    
    def __self__(self):
        return f"{self.name}"
        

class Salesman(models.Model):
    salesman_fname = models.CharField(max_length=45)
    salesman_lname = models.CharField(max_length=45)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    
    def __self__(self):
        return f"{salesman_fname} {salesman_lname}"
        

class Hypothecation(models.Model):
    hypothecation = models.CharField(max_length = 25)
    hypothecationfullname = models.CharField(max_length = 65)
    
    def __self__(self):
        return f"{hypothecation}"
        

class Taxation(models.Model):
    tax_regime = models.CharField(max_length=25)
    tax_slab = models.CharField(max_length=45)
    tax_subcategory_a_name =models.CharField(max_length=35)
    tax_subcategory_a_percent =models.DecimalField(max_digits=4, decimal_places=2)
    tax_subcategory_b_name =models.CharField(max_length=35)
    tax_subcategory_b_percent =models.DecimalField(max_digits=4, decimal_places=2)
    tax_start_date =models.DateField()
    tax_end_date =models.DateField(default=date(2099,7,1))    
    tax_active = models.BooleanField(default=True)
    
    def __self__(self):
        return f"{tax_slab} {tax_subcategory_a_percent}%"
        

class Remark(models.Model):
    remark = models.CharField(max_length = 55)
    
    def __self__(self):
        return f"{remark}"
        
        
class Branch(models.Model):
    branch_name =models.CharField(max_length=55)
    branch_contact_person =models.CharField(max_length=65)
    branch_contact =models.CharField(max_length=10)
    branch_email =models.EmailField(max_length=65)
    branch_location =models.CharField(max_length=65)
    branch_address_l =models.CharField(max_length=65)
    branch_address_2 =models.CharField(max_length=65)
    branch_company =models.ForeignKey(Company,on_delete=models.CASCADE)
    
    def __self__(self):
        return f"{self.branch_name}"
    
    
    
    
    
    
    
    
    