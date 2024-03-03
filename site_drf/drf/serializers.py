from rest_framework import serializers

from site_drf.drf.models import Sitedrf


class DogSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Sitedrf
        fields = "__all__"
