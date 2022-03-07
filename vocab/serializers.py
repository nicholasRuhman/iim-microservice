from rest_framework import serializers
from .models import Vocab


class VocabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocab
        fields = ('vocab',)

    #def to_representation(self, instance):
  #      return instance.vocab
