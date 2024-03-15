from rest_framework import serializers
from .models import ShareHolderFuns,ShareHolderName,RdPerson,RDCollection,LoanPerson,LoanCollection,LoanAmount,RDIntrest,RDCollectionNew,LoanCollectionNew

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


class ShareHolderFunsDataDisSerializer(serializers.Serializer):
    sh_name = serializers.CharField(source='sh_name.name')
    Sh_id = serializers.CharField(source='sh_name.Sh_id')
    shf_id = serializers.IntegerField()
    amount_credit = serializers.FloatField()
    amount_Debit = serializers.FloatField(default=0.0, allow_null=True)
    time = serializers.DateTimeField()


class RDCollectionSerializerData(serializers.ModelSerializer):
    person_id = serializers.IntegerField(source='person.rdp_id')
    person_name = serializers.CharField(source='person.name')
    class Meta:
        model = RDCollection
        fields = ['id', 'person_id', 'person_name', 'amount_collected', 'remarks', 'collection_date']


class LoanCollectionSerilizerData(serializers.ModelSerializer):
    person_id = serializers.IntegerField(source='loan_person.loan_id')
    person_name = serializers.CharField(source='loan_person.name')
    class Meta:
        model= LoanCollection
        fields =['id','person_id', 'person_name', 'amount_collected', 'remarks', 'collection_date']




class RdIntersetSerilizer(serializers.ModelSerializer):
    person_name= serializers.CharField(source='person.name')
    person_id= serializers.IntegerField(source='person.rdp_id')
    class Meta:
        model = RDIntrest
        fields =['rd_intrest_id' ,'person_name','person_id','start_date','closing_date','is_active','duration','interest_rate']

    
class RdIntersetOrignalSerilizer(serializers.ModelSerializer):
    class Meta:
        model = RDIntrest
        fields = '__all__'


class RDColloectionNewSerilizer(serializers.ModelSerializer):
    class Meta:
        model = RDCollectionNew
        fields = '__all__'


class RDCollectionNewDataSerializer(serializers.ModelSerializer):
    person_name= serializers.CharField(source='rd_intrest.person.name')
    person_id = serializers.IntegerField(source='rd_intrest.person.rdp_id')
    class Meta:
        model = RDCollectionNew
        fields = ['rd_intrest','person_name','person_id','amount_collected','user','remarks','collection_date']



class RDCollectionNewDataallSerializer(serializers.ModelSerializer):
    person_name= serializers.CharField(source='rd_intrest.person.name')
    person_id = serializers.IntegerField(source='rd_intrest.person.rdp_id')
    duration= serializers.IntegerField(source='rd_intrest.duration')
    interest = serializers.IntegerField(source='rd_intrest.interest_rate')
    start_date = serializers.CharField(source='rd_intrest.start_date')
    closing_date = serializers.CharField(source='rd_intrest.closing_date')
    is_active = serializers.BooleanField(source='rd_intrest.is_active')
    class Meta:
        model = RDCollectionNew
        fields = ['rd_intrest','person_name','duration','interest','is_active','start_date','closing_date','person_id','amount_collected','user','remarks','collection_date']


    
class LaonaAmountIntrestSerilizer(serializers.ModelSerializer):
    person_id = serializers.IntegerField(source='loan_person.loan_id')
    person_name = serializers.CharField(source='loan_person.name')
    class Meta:
        model = LoanAmount
        fields = ['id','person_id','person_name','closing_date','duration','interest_rate','is_active','loan_amount','loan_person','opening_date','remarks','start_date','time','user']


class LoanCollectionNewSerilizer(serializers.ModelSerializer):
    class Meta:
        models = LoanCollectionNew
        fields = '__all__'


class LoanCollectionNewDataallSerializer(serializers.ModelSerializer):
    person_name= serializers.CharField(source='loan_intrest.loan_person.name')
    person_id = serializers.IntegerField(source='loan_intrest.loan_person.loan_id')
    loan_amount = serializers.IntegerField(source='loan_intrest.loan_amount')
    is_active = serializers.BooleanField(source='loan_intrest.is_active')
    duration= serializers.IntegerField(source='loan_intrest.duration')
    start_date = serializers.CharField(source='loan_intrest.start_date')
    closing_date = serializers.CharField(source='loan_intrest.closing_date')
    interest = serializers.IntegerField(source='loan_intrest.interest_rate')
    class Meta:
        model = LoanCollectionNew
        fields = ['person_name','person_id','loan_amount','is_active','duration','start_date','closing_date','interest','loan_intrest','collection_date','amount_collected','remarks']


class LoanCollectionNewDataSerializer(serializers.ModelSerializer):
    person_name= serializers.CharField(source='loan_intrest.loan_person.name')
    person_id = serializers.IntegerField(source='loan_intrest.loan_person.loan_id')
    class Meta:
        model = LoanCollectionNew
        fields = ['person_name','person_id','loan_intrest','collection_date','amount_collected','remarks','user']