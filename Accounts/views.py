from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializers import Todoserializer
from rest_framework import status
from .models import Todo

# Create your views here.
@api_view(["POST"])
def create(request):
    serializer = Todoserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Todo Create Successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



