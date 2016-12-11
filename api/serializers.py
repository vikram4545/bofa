from rest_framework import serializers
from boapp.models import Number, Holder


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = '__all__'


class HolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holder
        fields = '__all__'
