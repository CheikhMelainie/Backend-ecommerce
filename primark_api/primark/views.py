from unicodedata import category
from django.shortcuts import render
from .models import AuthUser, Produit,UserProfile,Category,Favorite
from .serializers import CategorySerializer,FavoritSerializer,ProduiSerializer,UserprofileSerializer,UserSerializers
from rest_framework.decorators import api_view
from rest_framework import status,filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate, login

# Create your views here.

#*************************************************************************************************
class LoginView(APIView):
    permission_classes = ()
    def post(self, request,):
       username = request.data.get("username")
       password = request.data.get("password")
       user = authenticate(username=username, password=password)
       if user:
           return Response({"token": user.auth_token.key})
       else:
           return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializers

#*************************************************************************************************


@api_view(['GET','POST'])
def Produit_List(request):
    #GET
    if request.method == 'GET':
        produits = Produit.objects.all()
        serializer = ProduiSerializer(produits,many=True)
        return Response(serializer.data)
        permission_classes = ['IsAuthentication']
    #POST
    elif request.method == 'POST':
        serializer = ProduiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','PUT','DELETE'])
def Produit_List_pk(request,pk):
    try:
     produit = Produit.objects.get(pk=pk)
    except Produit.DoesNotExists:
         return Response(status=status.HTTP_404_NOT_FOUND)
    #GET
    if request.method == 'GET':
        serializer = ProduiSerializer(produit)
        return Response(serializer.data)
    #PUT
    elif request.method == 'PUT':
        serializer = ProduiSerializer(produit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    #DELETE
    if request.method == 'DELETE':
        produit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def Categoy_List(request):
    if request.method == 'GET':
     categories = Category.objects.all()
     serializer = CategorySerializer(categories,many=True)
     return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','PUT','DELETE'])
def Categoy_List_pk(request,pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #GET
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CategorySerializer(category,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    #DELETE
    if request.methode == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
