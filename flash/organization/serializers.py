from rest_framework import serializers

from flash.organization.models import Organization, Filial
from flash.organization.validators import rating_validator


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'name', 'description', 'logo',)


class NestedFilialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filial
        fields = ('id', 'address',)


class FilialSerializer(NestedFilialSerializer):
    organization = OrganizationSerializer(read_only=True)

    class Meta(NestedFilialSerializer.Meta):
        fields = NestedFilialSerializer.Meta.fields + ('organization',)


class OrganizationRateSerializer(serializers.Serializer):
    value = serializers.IntegerField(validators=[rating_validator])

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        instance.rate(validated_data.get('value'))

        return instance
