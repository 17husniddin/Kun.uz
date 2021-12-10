from rest_framework import serializers
from aloqa.models import *


class AloqaSerializer(serializers.ModelSerializer):
    class Meta():
        model = Aloqa
        fields = '__all__'