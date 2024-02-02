from rest_framework import serializers
from . models import GRN,MIR,MaterialIssue
from material.models import PurchaseOrder



class GRNSerilizer(serializers.ModelSerializer):
    class Meta:
        model = GRN
        fields = '__all__'


class MiroSerilizer(serializers.ModelSerializer):
    class Meta:
        model= MIR
        fields = '__all__'


class MaterialIssueSerilizer(serializers.ModelSerializer):
    class Meta:
        model = MaterialIssue
        fields ='__all__'


class POinsertinIRNserilizer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ['po_no','user','time','vendor_address','delivery_address','item_pr']