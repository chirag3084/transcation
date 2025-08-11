from rest_framework import serializers
from .models import Transcation

class TranscationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transcation
        fields = ["id","date_t","amount_t","category_t","description_t"]