from rest_framework import serializers
# from views import *
from ..models import *

class ReviewSerializers(serializers.ModelSerializer):
    apiuser = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        exclude = ('id','car')
        # fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    discount_price = serializers.SerializerMethodField()
    Reviews = ReviewSerializers(many=True, read_only=True)
    class Meta:
        model = Carlist
        exclude = ['id','activate']
        # fields = '__all__'
    
    def get_discount_price(self, object):
        return object.price - 5000
    
   
    
    def validated_price(self, value):
        if value < 20000:
            raise serializers.ValidationError('Price must be greater than 20000')
        return value
    
    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and Description must be different')
        return data
    
class ShowroomSerializer(serializers.ModelSerializer):
    # showrooms = CarSerializer(many=True, read_only=True)
    # showrooms = serializers.StringRelatedField(many=True)
    # showrooms = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    showrooms = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='car_detail')
    class Meta:
        model = Showroomlist
        fields = '__all__'


