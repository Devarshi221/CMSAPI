from rest_framework import serializers

from .models import *

class userserializers(serializers.ModelSerializer):
    class Meta:
        model = user
        #fields =[all filed name what we want]
        #exclude =['Name']
        fields= '__all__'


class postserializers(serializers.ModelSerializer):
    class Meta:
        model = Post_blog
        fields= '__all__'

class Likeserializers(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields= '__all__'

