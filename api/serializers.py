from rest_framework import serializers
from api.models import Subscription

class CoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id','name', 'cpf', 'email', 'phone', 'created_at']

    def create(self, validated_data):
        return Subscription.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('ID', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance