from rest_framework import serializers
from .models import ShareHolderFuns,ShareHolderName,RdPerson,RDCollection,LoanPerson,LoanCollection,LoanAmount

class ShareHolderFunsSerilizer(serializers.ModelSerializer):
    class Meta:
        model = ShareHolderFuns
        fields = '__all__'


class ShareHolderNameSerilizer(serializers.ModelSerializer):
    class Meta:
        model = ShareHolderName
        fields = '__all__'


class SerilzerHOlderFund(serializers.Serializer):
    shf_id = serializers.IntegerField()
    name = serializers.CharField()
    totalInvested = serializers.FloatField()

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = RdPerson
        fields = '__all__' 

class RDCollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = RDCollection
        fields = ['person','amount_collected','user','remarks','collection_date']
        
class RDCollectionDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RDCollection
        fields = ['person','amount_collected','user','remarks','collection_date']





class LoanPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanPerson
        fields = '__all__' 

class LoanCollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = LoanCollection
        fields = '__all__'
        
class LoanCollectionDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LoanCollection
        fields = ['loan_person','amount_collected','user','remarks','collection_date']



# loan Amount 

class LaonaAmountSerilizer(serializers.ModelSerializer):
    class Meta:
        model = LoanAmount
        fields = '__all__'
