


from rest_framework import serializers
from goods.models import SpecificationOption



class OptModelSerializer(serializers.ModelSerializer):
    spec = serializers.StringRelatedField() # read_only=True
    spec_id = serializers.IntegerField()

    class Meta:
        model = SpecificationOption
        fields = [
            'id', # read_only=True
            'value',
            'spec',
            'spec_id'
        ]