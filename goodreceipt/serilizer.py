from rest_framework import serializers
from . models import GRN



class GRNSerilizer(serializers.ModelSerializer):
    class Meta:
        model = GRN
        fields = '__all__'