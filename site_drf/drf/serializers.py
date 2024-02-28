from rest_framework import serializers

from site_drf.drf.models import Sitedrf


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sitedrf
        fields = ('title', 'cat_id')
