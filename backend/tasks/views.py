from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import TaskSerializer
from .models import Task

class PostListAPI(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message':'Task created successfully.'
            },status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        tasks=Task.object.all().order_by('-completion_date')