from django.contrib import admin
from pages.models import Colors,Salesman,Company,Hypothecation,Taxation,Remark,Branch

# Register your models here.

class ColorsAdmin(admin.ModelAdmin):
    list_display=("id","name",)
    verbose_name_plural = "colors"
    
class SalesmanAdmin(admin.ModelAdmin):
    list_display =("id","salesman_fname","salesman_lname")
    
class CompanyAdmin(admin.ModelAdmin):
    list_display=("id","company_name","company_primary_contact","company_secondary_contact",)
    verbose_name_plural = "Company"
    
class HypothecationAdmin(admin.ModelAdmin):
    list_display = ("id","hypothecation","hypothecationfullname",)
    
class TaxationAdmin(admin.ModelAdmin):
    list_display=("id","tax_slab","tax_subcategory_a_name","tax_subcategory_a_percent","tax_subcategory_b_name","tax_subcategory_b_percent","tax_active",)
 
class RemarkAdmin(admin.ModelAdmin):
    list_display = ("id","remark",)
 
class BranchAdmin(admin.ModelAdmin):
    list_display = ("id","branch_name","branch_contact_person","branch_contact",) 
    
admin.site.register(Colors,ColorsAdmin)
admin.site.register(Salesman,SalesmanAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Hypothecation,HypothecationAdmin)
admin.site.register(Taxation,TaxationAdmin)
admin.site.register(Remark,RemarkAdmin)
admin.site.register(Branch,BranchAdmin)
