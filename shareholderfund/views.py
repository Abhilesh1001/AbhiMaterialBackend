from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serilizer import ShareHolderFunsSerilizer,ShareHolderNameSerilizer,SerilzerHOlderFund,RDCollectionSerializer,PersonSerializer
from .models import ShareHolderFuns,ShareHolderName,RdPerson,RDCollection
from rest_framework.permissions import IsAuthenticated
from cusauth.renderers import UserRenderer



# Create your views here.
def index(request):
    return HttpResponse('ok')


class ShreHolderFundView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serilizer =  ShareHolderFunsSerilizer(data=request.data,many= True)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'data creates Successfully'},status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors)
        
    def get(self,request,pk=None,format=None):

        if pk is not None:
            sh = ShareHolderFuns.objects.get(Sh_id=pk)
            serilizer =  ShareHolderFunsSerilizer(sh)
            return Response(serilizer.data,status=status.HTTP_200_OK)
        else:
            sh = ShareHolderFuns.objects.all()
            serilizer =  ShareHolderFunsSerilizer(sh,many= True)
            return Response(serilizer.data,status=status.HTTP_200_OK)

        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None,format=None):
        sh = ShareHolderFuns.objects.get(Sh_id=pk)
        serilizer = ShareHolderFunsSerilizer(sh,data=request.data)
        if  serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_200_OK)
        
    def patch(self,request,pk=None,format=None):
        sh = ShareHolderFuns.objects.get(Sh_id=pk)
        serilizer = ShareHolderFunsSerilizer(sh,data=request.data)
        if  serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_200_OK)
        
    def put(self,request,pk=None,format=None):
        sh = ShareHolderFuns.objects.get(Sh_id=pk)
        serilizer = ShareHolderFunsSerilizer(sh,data=request.data)
        if  serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_200_OK)
        

class ShreHolderNameView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        print(request.data)
        serilizer = ShareHolderNameSerilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Holder created Successfully','data':serilizer.data},status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors)
        
        
    def get(self,request,pk=None,format=None):

        if pk is not None:
            sh = ShareHolderName.objects.get(Sh_id=pk)
            serilizer =  ShareHolderNameSerilizer(sh)
            return Response(serilizer.data,status=status.HTTP_200_OK)
        else:
            sh = ShareHolderName.objects.all()
            serilizer =  ShareHolderNameSerilizer(sh,many= True)
            return Response(serilizer.data,status=status.HTTP_200_OK)
        
        


    def put(self,request,pk=None,format=None):
        sh = ShareHolderName.objects.get(Sh_id=pk)
        serilizer = ShareHolderNameSerilizer(sh,data=request.data)
        if  serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self,request,pk=None,format=None):
        sh = ShareHolderFuns.objects.get(Sh_id=pk)
        serilizer = ShareHolderNameSerilizer(sh,data=request.data)
        if  serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None,format=None):
        sh = ShareHolderName.objects.get(Sh_id=pk)
        serilizer = ShareHolderNameSerilizer(sh,data=request.data)
        if  serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
        

from collections import defaultdict
def shfview():
    shf_objects = ShareHolderFuns.objects.all()

    orignal_pr_line = defaultdict(float)

    for shf_item in shf_objects:  
        print(shf_item.sh_name.Sh_id,shf_item.amount_credit,shf_item.amount_Debit)
        orignal_pr_line[shf_item.sh_name.Sh_id] += shf_item.amount_credit - shf_item.amount_Debit

    dictval = []    
    for item in orignal_pr_line:
        shname =  ShareHolderName.objects.get(Sh_id=item)
        dict = {
            'shf_id': item,
            'name':shname.name,
            'totalInvested' : orignal_pr_line[item]
        }  
        dictval.append(dict)  
    
    return dictval
    



class CapitalDisclouserview(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        sh=shfview()
        serilizer =  SerilzerHOlderFund(sh,many= True)
        print(serilizer.data)
        return Response(serilizer.data,status=status.HTTP_200_OK)
    


class RDCollectionBulkCreateView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        data = request.data
        serializer = RDCollectionSerializer(data=data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,pk=None,format=None):
        if pk is not None:
            rd = RDCollection.object.get(pk=pk)
            serilizer =  RDCollectionSerializer(rd)
            return Response(serilizer.data)
        else:
            rd = RDCollection.objects.all()
            serilizer = RDCollection(rd,many=True)
            return Response(serilizer.data)

    def put(self,request,pk=None,format=None):
        rd = RDCollection.objects.get(pk=pk)
        serilizer = RDCollectionSerializer(rd,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
    def patch(self,request,pk=None,format=None):
        rd = RDCollection.objects.get(pk=pk)
        serilizer = RDCollectionSerializer(rd,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        
           
class RdName(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serilizer = PersonSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Rd person created Successfully','data':serilizer.data},status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors)
    
    def get(self,request,pk=None,format=None):
        if pk is not None:
            rdp= RdPerson.objects.get(pk=pk)
            serilizer =  PersonSerializer(rdp)
            return Response(serilizer.data)
        else:
            rpd =RdPerson.objects.all()
            serilizer = PersonSerializer(rpd,many=True)
            return Response(serilizer.data)
        
    def put(self,request,pk=None,format=None):
        rpd =  RdPerson.objects.get(pk=pk)
        serilizer = PersonSerializer(rpd,data=request.data) 
        if  serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk=None,format=None):
        rpd =  RdPerson.objects.get(pk=pk)
        serilizer = PersonSerializer(rpd,data=request.data) 
        if  serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)




        