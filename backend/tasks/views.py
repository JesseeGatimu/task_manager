from .models import Task
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class TaskListCreateAPI(APIView):
    permission_classes=['IsAuthenticated']
    #create a single task
    def post(self,request):
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid:
            serializer.save(user=request.user)
            return Response({
                "message":"Task Created",
                "data":serializer.data
            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    #fetch all tasks 
    def get(self,request):
        tasks=Task.objects.filter(user=request.user).order_by('-completion_date')
        serializer=TaskSerializer(tasks,many=True)
        return Response({
            "message":"Tasks fetched successfully",
            "data":serializer.data
        },status=status.HTTP_200_OK)

class TaskDetailAPI(APIView):
    permissions_classes=['IsAuthenticated']

    #get a single task
    def get(self,request,pk):
        task=get_object_or_404(Task,pk=pk,user=request.user)
        serializer=TaskSerializer(task)
        return Response({
            "message":"Task fetched successfully",
            "data":serializer.data
        })

    #fully update of a task
    def put(self,request,pk):
        task=get_object_or_404(Task,pk=pk,user=request.user)
        serializer=TaskSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({
                "message":"Task fully updated",
                "data":serializer.data
            },status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    #partially updating a task
    def patch(self,request,pk):
        task=get_object_or_404(Task,pk=pk,user=request.user)
        serializer=TaskSerializer(task,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({
                "message":"Patch successful",
                "data":serializer.data
            },status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    #task deletion
    def delete(self,request,pk):
        task=get_object_or_404(Task,pk=pk,user=request.user)
        task.delete()
        return Response({
            "message":"Deleted successfully"
        },status=status.HTTP_200_OK)