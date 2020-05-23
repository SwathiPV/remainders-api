from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Remainder
from .serializers import RemainderSerializer

@csrf_exempt
def remainder_list(request):

    if request.method == 'GET':
        remainders = Remainder.objects.all()
        serializer = RemainderSerializer(remainders, many=True)
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RemainderSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def remainder_detail(request, pk):
    try:
        remainder = Remainder.objects.get(pk=pk)
    except Remainder.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RemainderSerializer(remainder)
        return JsonResponse(serializer.data)

    elif  request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RemainderSerializer(remainder, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        remainder.delete()
        return HttpResponse(status=204)