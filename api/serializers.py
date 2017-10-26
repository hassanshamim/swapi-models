from rest_framework.serializers import ModelSerializer

from .models import Planet

class PlanetSerializer(ModelSerializer):

    class Meta:
        model = Planet
        # our subset of fields we want to make available.  Defaults to all fields.
        fields = ('id', 'name', 'population')