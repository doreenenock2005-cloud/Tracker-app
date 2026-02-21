from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view (['POST','GET','PUT','DELETE',])
def user(request):
    if request.method == 'GET':
       record = StudyRecord.objects.all()
       serializers= SubjectSerializer(record ,many=True)
       return Response(serializers.data)
        
        
    if request.method== 'POST':
        serializers = SubjectSerializer(data = request.data)
        if serializers.is_valid(): 
            serializers.save()
            return Response(serializers.data,status=201)
        return Response(serializers.data,status=400)

def update(request):
    if request=='PUT':
        record =StudyRecord.objects.all(Id=id)
        serializers = SubjectSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data,status = 201)
    return Response(serializers.data,status = 400)
def delete_item(request):
    if request.method =='DELETE':
        record = StudyRecord.objects.all()
        record.delete()
        return Response({"message":"record successfully deleted"})   