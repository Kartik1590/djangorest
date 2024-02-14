from rest_framework import serializers

from watchlist_app.models import WatchList
from watchlist_app.models import StreamingPlatform, Review

# def description_words(value):
#     if len(value)<3:
#         raise serializers.ValidationError("Description needs atleast 200 words")
#     return value


# class MovieSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField()
#     description=serializers.CharField(validators=[description_words])
#     active=serializers.BooleanField()
    
#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.description=validated_data.get('description',instance.description)
#         instance.active=validated_data.get('active',instance.active)
#         instance.save()
#         return instance
    
    # def validate(self,data):  #class level validation it can validate different feilds
    #     if data['name']==data['description']:
    #         raise serializers.ValidationError("Title and description should be different")
    #     return data
    
    # def validate_name(self,value): # feild level validation
    #     if len(value)<3:
    #         raise serializers.ValidationError("Name is too short")
    #     return value


# Model serializer

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields="__all__"

class WatchSerializer(serializers.ModelSerializer):
    
    review=ReviewSerializer(many=True,read_only=True)
    len_name=serializers.SerializerMethodField()   #Custom feilds
    class Meta:
        model=WatchList
        fields="__all__"
        #exclude=['active']
        
    def get_len_name(self,object):
        val=object.title.replace(' ','')
        return len(val)
    
    
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist=WatchSerializer(many=True,read_only=True) # Nested serializer
    class Meta:
        model=StreamingPlatform
        fields="__all__"
        
        
    # def validate(self,data):  #class level validation it can validate different feilds
    #     if data['name']==data['description']:
    #         raise serializers.ValidationError("Title and description should be different")
    #     return data
    
    # def validate_name(self,value): # feild level validation
    #     if len(value)<3:
    #         raise serializers.ValidationError("Name is too short")
    
    #     return value
    
    

    
