from rest_framework import serializers
from .models import Reference

class ReferenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reference
        # fields = ('quote', 'author', 'source', 'tags', 'pub_date')
        fields = '__all__'

    def create(self, validated_data):
        return Reference.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.quote = validated_data.get('quote', instance.quote)
        instance.author = validated_data.get('author', instance.author)
        instance.source = validated_data.get('source', instance.source)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.save()

        return instance