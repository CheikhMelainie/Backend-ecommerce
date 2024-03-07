from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from primark.models import AuthUser,Category,Favorite,Produit,UserProfile



class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
            user = User(
                email = validated_data['email'],
                username =validated_data['username']
            )
            user.set_password(validated_data['password'])
            user.save()
            Token.objects.create(user=user)
            return user


class ProduiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields ='__all__'

class FavoritSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class UserprofileSerializer(serializers.ModelSerializer):
    class meta:
        model = UserProfile
        fields ='__all__'