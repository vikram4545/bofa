from django.shortcuts import render
from boapp.models import Number, Holder
from .serializers import NumberSerializer, HolderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class NumberSerializerView(APIView):
    def get(self,request):
        number = Number.objects.all()
        serializer=NumberSerializer(number,many= True )
        return Response(serializer.data)


class HolderSerializerView(APIView):
    def get(self,request):
        holder=Holder.objects.all()
        serializerh=HolderSerializer(holder,many=True)
        return Response(serializerh.data)

