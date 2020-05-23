from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Remainder
from .serializers import RemainderSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def remainder_list(request):

    if request.method == 'GET':
        remainders = Remainder.objects.all()
        serializer = RemainderSerializer(remainders, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = RemainderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def remainder_detail(request, pk):
    try:
        remainder = Remainder.objects.get(pk=pk)
    except Remainder.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RemainderSerializer(remainder)
        return Response(serializer.data)

    elif  request.method == 'PUT':
        serializer = RemainderSerializer(remainder, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        remainder.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)