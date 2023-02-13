from django.http import JsonResponse, HttpResponse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from .models import Gal
import os

# Create your views here.
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token
 
 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def index(req):
    return Response('hello')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def private(req):
    return Response("private area")    

# Gal crud

class GalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gal
        fields = '__all__'


@permission_classes([IsAuthenticated])
class GalView(APIView):

    def get(self, request):
            usr = request.user
            my_model = usr.gal_set.all()
            serializer = GalSerializer(my_model, many=True)
            return Response(serializer.data)

    def post(self, request):
        # usr =request.user
        # print(usr)
        serializer = GalSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def put(self, request, pk):
     
        my_model = Gal.objects.get(pk=pk)
        serializer = GalSerializer(my_model, data=request.data)
        if os.path.isfile(my_model.image.path):
            os.remove(my_model.image.path)
            my_model.delete()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self, request, pk):
        my_model = Gal.objects.get(pk=pk)
        if os.path.isfile(my_model.image.path):
            os.remove(my_model.image.path)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Gallery CRUD - end