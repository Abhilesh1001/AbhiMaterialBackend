from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import GRN
from .serilizer import GRNSerilizer
from cusauth.models import User
from cusauth.renderers import UserRenderer
from  rest_framework.permissions import IsAuthenticated

# Create your views here.

def index(request):
    return HttpResponse('ok')


class GRNView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]
    def post(self,request,format=None):
        serilizer = GRNSerilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Data Created Sussfully','data':serilizer.data},status=status.HTTP_201_CREATED)
        
        return Response(serilizer.errors)
    
    def get(self,request,pk=None,format=None):
        if pk is not None:
            grn = GRN.objects.get(grn_no = pk)
            serilzer =  GRNSerilizer(grn)
            return Response(serilzer.data,status=status.HTTP_200_OK)
        else:
            grn = GRN.objects.all()
            serilzer =GRNSerilizer(grn,many=True)
            return Response(serilzer.data,status=status.HTTP_200_OK)

    def put(self,request,pk=None,format=None):
        grn = GRN.objects.get(grn_no=pk)
        serilizer =  GRNSerilizer(grn,data=request.data)        
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Data Updated Sussfully','data':serilizer.data},status=status.HTTP_200_OK)
        return Response(serilizer.errors)
    
    def patch(self,request,pk=None,format=None):
        grn = GRN.objects.get(grn_no=pk)
        serilizer =  GRNSerilizer(grn,data=request.data) 
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Data Updated Sussfully','data':serilizer.data},status=status.HTTP_200_OK)
        return Response(serilizer.errors)


