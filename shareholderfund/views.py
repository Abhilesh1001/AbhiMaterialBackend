from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serilizer import ShareHolderFunsSerilizer,ShareHolderNameSerilizer,SerilzerHOlderFund,RDCollectionSerializer,RDCollectionDataSerializer,PersonSerializer,LoanCollectionDataSerializer,LoanCollectionSerializer,LoanPersonSerializer,LaonaAmountSerilizer
from .models import ShareHolderFuns,ShareHolderName,RdPerson,RDCollection,LoanCollection,LoanPerson,LoanAmount
from rest_framework.permissions import IsAuthenticated
from cusauth.renderers import UserRenderer



# Create your views here.
def index(request):
    return HttpResponse('ok')


class ShreHolderFundView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serilizer =  ShareHolderFunsSerilizer(data=request.data)
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
        amount_credit = float(shf_item.amount_credit) if shf_item.amount_credit else 0
        amount_debit = float(shf_item.amount_Debit) if shf_item.amount_Debit else 0
        orignal_pr_line[shf_item.sh_name.Sh_id] += amount_credit - amount_debit

    dictval = []    
    for item in orignal_pr_line:
        shname = ShareHolderName.objects.get(Sh_id=item)
        dict_entry = {
            'shf_id': item,
            'name': shname.name,
            'totalInvested': orignal_pr_line[item]
        }  
        dictval.append(dict_entry) 
    
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
    def post(self, request, format=None):
        serializer = RDCollectionSerializer(data=request.data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data has saved Successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
    
    def get(self,request,pk=None,format=None):
        if pk is not None:
            rd = RDCollection.object.get(pk=pk)
            serilizer =  RDCollectionSerializer(rd)
            return Response(serilizer.data)
        else:
            rd = RDCollection.objects.all()
            serilizer = RDCollectionSerializer(rd,many=True)
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



from django.utils.timezone import make_aware
from datetime import datetime
class RDDataAPIView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        start_date = request.data.get('start_date')  # Format: 'YYYY-MM-DD'
        end_date = request.data.get('end_date')      # Format: 'YYYY-MM-DD'
        start_date_aware = make_aware(datetime.strptime(start_date, '%Y-%m-%d'))
        end_date_aware = make_aware(datetime.strptime(end_date, '%Y-%m-%d'))
        print(start_date_aware, end_date_aware)
        rd_collections = RDCollection.objects.filter(collection_date__range=(start_date_aware, end_date_aware))
        serializer = RDCollectionDataSerializer(rd_collections, many=True)

        # Organize data as needed
        organized_data = self.organize_data(serializer.data)

        return Response(organized_data, status=status.HTTP_200_OK)

    def organize_data(self, serialized_data):
        # Implement logic to organize data as needed
        # For example, create a dictionary with names as keys and lists of amounts as values

        organized_data = {}

        for item in serialized_data:
            person_id = item.get('person')
            amount_collected = item['amount_collected']
            collection_date = item['collection_date']

            if person_id and amount_collected and collection_date:
                # Use the person_id to fetch the associated person's name
                person_name = RdPerson.objects.get(rdp_id=person_id).name

                # Format the date to remove the time part
                formatted_date = collection_date.split('T')[0]

                if person_name not in organized_data:
                    organized_data[person_name] = {}

                if formatted_date not in organized_data[person_name]:
                    organized_data[person_name][formatted_date] = 0

                # Accumulate amounts for the same date and person
                organized_data[person_name][formatted_date] += float(amount_collected)

        return organized_data


# Loan Collection DAta 

class LoanCollectionBulkCreateView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = LoanCollectionSerializer(data=request.data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data has saved Successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
    
    def get(self,request,pk=None,format=None):
        if pk is not None:
            rd = LoanCollection.object.get(pk=pk)
            serilizer =  LoanCollectionSerializer(rd)
            return Response(serilizer.data)
        else:
            rd = LoanCollection.objects.all()
            serilizer = LoanCollectionSerializer(rd,many=True)
            return Response(serilizer.data)

    def put(self,request,pk=None,format=None):
        rd = LoanCollection.objects.get(pk=pk)
        serilizer = LoanCollectionSerializer(rd,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
    def patch(self,request,pk=None,format=None):
        rd = LoanCollection.objects.get(pk=pk)
        serilizer = LoanCollectionSerializer(rd,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        
           
class LoanName(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serilizer = LoanPersonSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Rd person created Successfully','data':serilizer.data},status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors)
    
    def get(self,request,pk=None,format=None):
        if pk is not None:
            rdp= LoanPerson.objects.get(pk=pk)
            serilizer =  LoanPersonSerializer(rdp)
            return Response(serilizer.data)
        else:
            rpd =LoanPerson.objects.all()
            serilizer = LoanPersonSerializer(rpd,many=True)
            return Response(serilizer.data)
        
    def put(self,request,pk=None,format=None):
        rpd =  LoanPerson.objects.get(pk=pk)
        serilizer = LoanPersonSerializer(rpd,data=request.data) 
        if  serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk=None,format=None):
        rpd =  LoanPerson.objects.get(pk=pk)
        serilizer = LoanPersonSerializer(rpd,data=request.data) 
        if  serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)



from django.utils.timezone import make_aware
from datetime import datetime
class LoanDataAPIView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        start_date = request.data.get('start_date')  # Format: 'YYYY-MM-DD'
        end_date = request.data.get('end_date')      # Format: 'YYYY-MM-DD'
        start_date_aware = make_aware(datetime.strptime(start_date, '%Y-%m-%d'))
        end_date_aware = make_aware(datetime.strptime(end_date, '%Y-%m-%d'))
        print(start_date_aware, end_date_aware)
        loan_collections = LoanCollection.objects.filter(collection_date__range=(start_date_aware, end_date_aware))
        serializer = LoanCollectionDataSerializer(loan_collections, many=True)

        # Organize data as needed
        organized_data = self.organize_data(serializer.data)

        return Response(organized_data, status=status.HTTP_200_OK)

    def organize_data(self, serialized_data):
        # Implement logic to organize data as needed
        # For example, create a dictionary with names as keys and lists of amounts as values

        organized_data = {}

        for item in serialized_data:
            person_id = item.get('loan_person')
            amount_collected = item['amount_collected']
            collection_date = item['collection_date']

            if person_id and amount_collected and collection_date:
                # Use the person_id to fetch the associated person's name
                person_name = LoanPerson.objects.get(loan_id=person_id).name

                # Format the date to remove the time part
                formatted_date = collection_date.split('T')[0]

                if person_name not in organized_data:
                    organized_data[person_name] = {}

                if formatted_date not in organized_data[person_name]:
                    organized_data[person_name][formatted_date] = 0

                # Accumulate amounts for the same date and person
                organized_data[person_name][formatted_date] += float(amount_collected)

        return organized_data


# loan amount 

class LaonAmountView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):
        serilizer = LaonaAmountSerilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Loan Amount Created','data':serilizer.data},status=status.HTTP_201_CREATED)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,pk=None,format=None):
        if pk is not None:
            loan = LoanAmount.objects.get(pk=pk) 
            serilizer =  LaonaAmountSerilizer(loan)
            return Response(serilizer.data,status=status.HTTP_200_OK)
        else:
            loan =LoanAmount.objects.all()
            serilizer = LaonaAmountSerilizer(loan,many=True)
            return Response(serilizer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk=None,format=None):
        loan =  LoanAmount.objects.get(pk=pk)
        serilizer = LaonaAmountSerilizer(loan,data=request.data) 
        if  serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk=None,format=None):
        loan =  LoanAmount.objects.get(pk=pk)
        serilizer = LaonaAmountSerilizer(loan,data=request.data) 
        if  serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

    