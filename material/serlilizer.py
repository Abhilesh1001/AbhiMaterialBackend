from rest_framework import serializers
from .models import Material,PurchaseRequestNew,Vendor,DeliveryAdress,PurchaseOrder




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