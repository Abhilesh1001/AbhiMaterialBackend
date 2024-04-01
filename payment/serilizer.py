from rest_framework import serializers
from .models import PaymentTovendor,AdvancePayment
from goodreceipt.models import MIR

class AdvancePaymentsErilizer(serializers.ModelSerializer):
    class Meta:
        model= AdvancePayment
        fields = '__all__'


class PaymentsErilizer(serializers.ModelSerializer):
    class Meta:
        model= PaymentTovendor
        fields = '__all__'


class AdvancePaymentsSerilizerChange(serializers.ModelSerializer):
    po_no = serializers.IntegerField(source='po_no.po_no')
    vendor_name = serializers.CharField(source='po_no.vendor_address')
    main_amount = serializers.CharField(source='po_no.maindata')
    class Meta:
        model= AdvancePayment
        fields = ['advance_payment_no','po_no','vendor_name','main_amount','amount_debit','user','time']


class PaymentSerilizerAll(serializers.ModelSerializer):
    item_grn = serializers.CharField(source='miro_no.item_grn')
    vendor_name = serializers.CharField(source='miro_no.vendor_address')
    bill_no = serializers.CharField(source='miro_no.billing')
    main_data = serializers.CharField(source='miro_no.maindata')

    class Meta:
        model= PaymentTovendor
        fields = ['payment_no','amount_debit','user','time','item_grn','vendor_name','bill_no','main_data','miro_no','advance_adjust']




class MiroSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model= MIR
        fields = '__all__'