from menu.models import Recipe
from rest_framework import serializers
from django.contrib.auth.models import User

from menu.models import Reviews


class RecipeSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')
    image = serializers.ImageField(required=False)
    class Meta:
        model = Recipe
        # fields = ['id','recipe_name','ingredients','instructions','cuisine','meal_type','image','image_url']
        fields = '__all__'

    def get_image_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.image.url
        return request.build_absolute_uri(photo_url)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    def create(self, validated_data):
        u=User.objects.create_user(username=validated_data['username'],
                                   password=validated_data['password'],
                                   email=validated_data['email'],
                                   first_name=validated_data['first_name'],
                                   last_name=validated_data['last_name'])
        return u


class ReviewSerializer(serializers.ModelSerializer):
    name=serializers.SerializerMethodField('get_user')
    recipe=serializers.SerializerMethodField('get_recipe')
    date=serializers.SerializerMethodField('get_date')
    class Meta:
        model = Reviews
        # fields = '__all__'
        fields = ['recipe','user','rating','comment','created_at','name','date']

    def get_user(self,obj):
        return obj.user.username

    def get_recipe(self,obj):
        return obj.recipe.recipe_name

    def get_date(self,obj):
        return obj.created_at.date()