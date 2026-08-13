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
    

@api_view(["GET", "PUT"])
def update(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response({'message': 'Todo Not Found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = Todoserializer(todo)
        return Response({'message': 'Todo Fetched Successfully', 'data': serializer.data}, status=status.HTTP_200_OK)

    
    serializer = Todoserializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Todo Update Successfully', 'data':serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    



