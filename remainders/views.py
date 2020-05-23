from .models import Remainder
from .serializers import RemainderSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class RemainderAPIView(APIView):
    def get(self, request):
        remainders = Remainder.objects.all()
        serializer = RemainderSerializer(remainders, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = RemainderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RemainderDetailsAPIView(APIView):
    def get_object(self, id):
        try:
            return Remainder.objects.get(pk=id)
        except Remainder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        remainder = self.get_object(id=pk)
        serializer = RemainderSerializer(remainder)
        return Response(serializer.data)

    def put(self, request, pk):
        remainder = self.get_object(id=pk)
        serializer = RemainderSerializer(remainder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        remainder = self.get_object(id=pk)
        remainder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


        

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def remainder_detail(request, pk):
    try:
        remainder = Remainder.objects.get(pk=pk)
    except Remainder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

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
        return Response(status=status.HTTP_204_NO_CONTENT)