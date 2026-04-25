from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import TaskSerializer
from .models import Task
from django.shortcuts import get_object_or_404

class TaskListAPI(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({
                'message':'Task created successfully.',
                'data':serializer.data
            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        tasks=Task.objects.filter(user=request.user).order_by('-completion_date','-id')
        serializer=TaskSerializer(tasks,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class TaskDetailAPI(APIView):
    permission_classes=[IsAuthenticated]
    # fetch a single task
    def get(self,request,pk):
        task=get_object_or_404(Task,pk=pk,user=request.user)
        serializer=TaskSerializer(task)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    #Update task(Full update)
    def put(self,request,pk):
        task=get_object_or_404(Task,pk=pk,user=request.user)
        serializer=TaskSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #Partial Update
    def patch(self,request,pk):
        task=get_object_or_404(Task,pk=pk,user=request.user)
        serializer=TaskSerializer(task,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #delete task
    def delete(self,request,pk):
        task=get_object_or_404(Task,pk=pk,user=request.user)
        task.delete()
        return Response({'message':'Deleted Successfully'},status=status.HTTP_200_OK)
