from rest_framework import serializers


from .models import Planet, People, Species

class PlanetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Planet
        # our subset of fields we want to make available.  Defaults to all fields.
        fields = ('id', 'name', 'population')


class PeopleSerializer(serializers.ModelSerializer):

    class Meta:
        model = People
        fields = ('id', 'name', 'birth_year', 'homeworld')


class SpeciesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Species
        fields = ('id', 'name', 'classification', 'homeworld', 'people')