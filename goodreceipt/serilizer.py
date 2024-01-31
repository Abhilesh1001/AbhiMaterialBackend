from rest_framework import serializers
from . models import GRN,MIR,MaterialIssue



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