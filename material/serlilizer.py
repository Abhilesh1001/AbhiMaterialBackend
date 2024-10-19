from rest_framework import serializers
from .models import Material,PurchaseRequestNew,Vendor,DeliveryAdress,PurchaseOrder,MaterialGroup,MaterialUnit,StoreLocation,CompanyAddress




class MaterialSerlizer(serializers.ModelSerializer):
    class Meta:
        model= Material
        fields = '__all__'


class PurchaseRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseRequestNew
        fields = '__all__'
        

class VendorSErilizer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class DeliverySerilizer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAdress
        fields = '__all__'

class PurchaseOrderSerilizer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'


class MaterialGroupSerilizer(serializers.ModelSerializer):
    class Meta:
        model = MaterialGroup
        fields = '__all__'


class MaterilUnitSerilizer(serializers.ModelSerializer):
    class Meta:
        model = MaterialUnit
        fields ="__all__"



class MaterilaStoreLocationSerilizer(serializers.ModelSerializer):
    class Meta:
        model =  StoreLocation 
        fields = "__all__"

    
class CompanyAddressSerilizer(serializers.ModelSerializer):
    class Meta:
        model= CompanyAddress
        fields = '__all__'

class DeliverySerilizerAll(serializers.ModelSerializer):
    company_s_no = serializers.IntegerField(source='company_address.s_no')
    company_name = serializers.CharField(source='company_address.name')
    company_address =  serializers.CharField(source='company_address.address')
    class Meta:
        model = DeliveryAdress
        fields = ['s_no','company_s_no','company_name','company_address','name','phone_no','vendor_name','gst','email','address']

        
