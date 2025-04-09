from django.http import Http404
from django.shortcuts import render
from django.template.defaulttags import comment
from rest_framework import viewsets
from menu.models import Recipe
from django.db.models import Q
from menu.serializers import RecipeSerializer,UserSerializer,ReviewSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from menu.models import Reviews


# Create your views here.
class RecipeView(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class FilterByCuisine(APIView):
    def get(self,request):
        query=self.request.query_params.get('filterkey')
        if query:
            items=Recipe.objects.filter(cuisine__icontains=query)
            if not items.exists():
                return Response({'msg':'No result found'},status=status.HTTP_200_OK)
            recipes=RecipeSerializer(items,many=True)
            return Response(recipes.data, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'No result found'}, status=status.HTTP_200_OK)


class FilterByIngredients(APIView):
    def get(self,request):
        query=self.request.query_params.get('filterkey')
        if query:
            items=Recipe.objects.filter(ingredients__icontains=query)
            if not items.exists():
                return Response({'msg':'No result found'},status=status.HTTP_200_OK)
            recipes=RecipeSerializer(items,many=True)
            return Response(recipes.data, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'No result found'}, status=status.HTTP_200_OK)


class FilterByMealType(APIView):
    def get(self,request):
        query=self.request.query_params.get('filterkey')
        if query:
            items=Recipe.objects.filter(meal_type__icontains=query)
            if not items.exists():
                return Response({'msg':'No result found'},status=status.HTTP_200_OK)
            recipes=RecipeSerializer(items,many=True)
            return Response(recipes.data, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'No result found'}, status=status.HTTP_200_OK)


class SearchRecipe(APIView):
    def get(self,request):
        query=self.request.query_params.get('searchkey')
        if query:
            items=Recipe.objects.filter(
                Q(cuisine__icontains=query)|
                Q(meal_type__icontains=query)|
                Q(ingredients__icontains=query)|
                Q(instructions__icontains=query)|
                Q(recipe_name__icontains=query)
            )
            if not items.exists():
                return Response({'msg':'No result found'},status=status.HTTP_200_OK)
            recipes=RecipeSerializer(items,many=True,context={"request":request})
            return Response(recipes.data, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'No result found'}, status=status.HTTP_200_OK)


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response({'msg':'Logout Successfully'},status=status.HTTP_200_OK)


class CreateReview(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        id=request.data['id']       #to fetch recipe id from json object received from client side
        c=request.data['comment']   #to fetch comment from json object
        r=request.data['rating']    #to fetch rating from json object
        u=self.request.user         #current login user

        recipe=Recipe.objects.get(id=id) #to fetch recipe details of particular recipe
        rev=Reviews.objects.create(user=u,recipe=recipe,comment=c,rating=r)
        rev.save()

        review=ReviewSerializer(rev) #converts it to json
        return Response(review.data,status=status.HTTP_201_CREATED)


class GetAllReviews(APIView):
    def get_object(self,pk):
        try:
            return Recipe.objects.get(id=pk)
        except:
            raise Http404
    def get(self,request,pk):
        r=self.get_object(pk)
        rev=Reviews.objects.filter(recipe=r)
        review=ReviewSerializer(rev,many=True)
        return Response(review.data,status=status.HTTP_200_OK)
