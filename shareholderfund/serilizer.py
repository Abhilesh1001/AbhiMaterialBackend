from rest_framework import serializers
from .models import ShareHolderFuns,ShareHolderName,RdPerson,RDCollection

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
        fields = ['id', 'name'] 

class RDCollectionSerializer(serializers.ModelSerializer):
    person = PersonSerializer()

    class Meta:
        model = RDCollection
        fields = ['id', 'person', 'collection_date', 'amount_collected', 'remarks']
