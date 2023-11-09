from .models import Viewer
from rest_framework import serializers

class ViewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viewer
        fields = '__all__'