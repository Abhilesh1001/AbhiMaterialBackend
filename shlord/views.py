from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from cusauth.renderers import UserRenderer
from .serilizer import PersonSerilizer,ShareHolderFunsSerilizer,ShareHolderFunsDataDisSerializer,SerilzerHOlderFund,RdIntersetOrignalSerilizer,RdIntersetSerilizer,RDColloectionSerilizer,RDCollectionDataallSerializer,RDCollectionDataSerializer,LaonaAmountSerilizer,LaonaAmountIntrestSerilizer,LoanCollectionSerilizer,LoanCollectionDataallSerializer,LoanCollectionDataSerializer
from .models import Person,LoanInt,LoanColl,ShareHolder,RDColl,RDInt
from collections import defaultdict
from django.utils.timezone import make_aware
from datetime import datetime

# Create your views here.
def index(request):
    return HttpResponse('ok')


class MemberView(APIView):

    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        print(request.data)
        serilizer = PersonSerilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Member Added successfully','data':serilizer.data},status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors)
        
        
    def get(self,request,pk=None,format=None):

        if pk is not None:
            sh = Person.objects.get(Sh_id=pk)
            serilizer =  PersonSerilizer(sh)
            return Response(serilizer.data,status=status.HTTP_200_OK)
        else:
            sh = Person.objects.all()
            serilizer =  PersonSerilizer(sh,many= True)
            return Response(serilizer.data,status=status.HTTP_200_OK)
        
    def put(self,request,pk=None,format=None):
        sh = Person.objects.get(Sh_id=pk)
        serilizer = PersonSerilizer(sh,data=request.data)
        if  serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self,request,pk=None,format=None):
        sh = PersonSerilizer.objects.get(Sh_id=pk)
        print(sh)
        serilizer = PersonSerilizer(sh,data=request.data)
        if  serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Holder Updated Successfully','data':serilizer.data},status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None,format=None):
        sh = Person.objects.get(Sh_id=pk)
        serilizer = PersonSerilizer(sh,data=request.data)
        if  serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class ShreHolderFundView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serilizer =  ShareHolderFunsSerilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Data creates Successfully'},status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors)
        
    def get(self,request,pk=None,format=None):

        if pk is not None:
            # get all data of pk person 
            
            sh = ShareHolder.objects.filter(person=pk)
            
            dict =  []
            for item in sh:
                print(item.amount_Debit)
                dict1= {
                    "name ":item.person.name,
                    "shf_id":item.shf_id,
                    "person_id":item.person.person_id,
                    "amount_credit":item.amount_credit,
                    "amount_Debit":item.amount_Debit,
                    "collection_date" : item.collection_date,
                    "time":item.time
                }

                dict.append(dict1)
            print(dict)

            serilizer =  ShareHolderFunsDataDisSerializer(sh,many=True)
            
            
            return Response(serilizer.data,status=status.HTTP_200_OK)
        else:
            sh = ShareHolder.objects.all()
            serilizer =  ShareHolderFunsDataDisSerializer(sh,many= True)
            return Response(serilizer.data,status=status.HTTP_200_OK)


    def put(self,request,pk=None,format=None):
        sh = ShareHolder.objects.get(Sh_id=pk)
        serilizer = ShareHolderFunsSerilizer(sh,data=request.data)
        if  serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_200_OK)
        
    def patch(self,request,pk=None,format=None):
        sh = ShareHolder.objects.get(Sh_id=pk)
        serilizer = ShareHolderFunsSerilizer(sh,data=request.data)
        if  serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_200_OK)
        
    def put(self,request,pk=None,format=None):
        sh = ShareHolder.objects.get(Sh_id=pk)
        serilizer = ShareHolderFunsSerilizer(sh,data=request.data)
        if  serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_200_OK)
      

def shfview():
    shf_objects = ShareHolder.objects.all()

    orignal_pr_line = defaultdict(float)

    for shf_item in shf_objects:
        amount_credit = float(shf_item.amount_credit) if shf_item.amount_credit else 0
        amount_debit = float(shf_item.amount_Debit) if shf_item.amount_Debit else 0
        orignal_pr_line[shf_item.person.person_id] += amount_credit - amount_debit

    dictval = []    
    for item in orignal_pr_line:
        shname = Person.objects.get(person_id=item)
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


class RDintrestView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):
        serilizer = RdIntersetOrignalSerilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'RD Intrest Created Successfully','data':serilizer.data},status=status.HTTP_201_CREATED)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,pk=None,format=None):
        if pk is not None:
            rdintrest = RDInt.objects.get(rd_id=pk) 
            serilizer = RdIntersetSerilizer(rdintrest)
            return Response(serilizer.data,status=status.HTTP_200_OK)
        else:
            rdintrest =RDInt.objects.all()
            serilizer = RdIntersetSerilizer(rdintrest,many=True)
            return Response(serilizer.data,status=status.HTTP_200_OK)
        
    def put(self,request,pk=None,format=None):
        rd =  RDInt.objects.get(rd_id=pk)
        serilizer = RdIntersetOrignalSerilizer(rd,data=request.data) 
        if  serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk=None,format=None):
        rd =  RDInt.objects.get(rd_id=pk)
        print(rd)
        serilizer = RdIntersetOrignalSerilizer(rd,data=request.data) 
        if  serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'RDIntrest Updated Successfully','data':serilizer.data},status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)



def merge_by_collection_date(queryset):
        merged_data = {}
        print('..........')
        for item in queryset:
            print(item.rd_interest)
            collection_date = item.collection_date.date()  # Extract date part
            rd_intrest_id = item.rd_interest.rd_id
            if (collection_date, rd_intrest_id) not in merged_data:
                merged_data[(collection_date, rd_intrest_id)] = item
            else:
                # If entry with same collection date and rd_intrest exists, add amount
                merged_data[(collection_date, rd_intrest_id)].amount_collected +=item.amount_collected
        return merged_data.values()




class RDcollectionView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):
        serilizer = RDColloectionSerilizer(data=request.data,many=True)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'RD Intrest Created Successfully','data':serilizer.data},status=status.HTTP_201_CREATED)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,pk=None,format=None):
        if pk is not None:
            rd_collections = RDColl.objects.filter(rd_interest=pk)
            merged_data = merge_by_collection_date(rd_collections)
            serilizer = RDCollectionDataallSerializer(merged_data,many=True)
            return Response(serilizer.data,status=status.HTTP_200_OK)
        else:   
            rdintrest =RDColl.objects.all()
            serilizer = RDColloectionSerilizer(rdintrest,many=True)
            return Response(serilizer.data,status=status.HTTP_200_OK)
        
    def put(self,request,pk=None,format=None):
        loan =  RDColl.objects.get(rd_collection_id=pk)
        serilizer = RDColloectionSerilizer(loan,data=request.data) 
        if  serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk=None,format=None):
        loan =  RDColl.objects.get(rd_collection_id=pk)
        serilizer = RDColloectionSerilizer(loan,data=request.data) 
        if  serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'RDcollection Updated Successfully','data':serilizer.data},status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

   
class RDDataAPIView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        start_date = request.data.get('start_date')  # Format: 'YYYY-MM-DD'
        end_date = request.data.get('end_date')      # Format: 'YYYY-MM-DD'
        start_date_aware = make_aware(datetime.strptime(start_date, '%Y-%m-%d'))
        end_date_aware = make_aware(datetime.strptime(end_date, '%Y-%m-%d'))
        print(start_date_aware, end_date_aware)
        rd_collections = RDColl.objects.filter(collection_date__range=(start_date_aware, end_date_aware))
        # print(rd_collections)
        serializer = RDCollectionDataSerializer(rd_collections, many=True)

        print(serializer.data)
        # Organize data as needed
        organized_data = self.organize_data(serializer.data)

        return Response(organized_data, status=status.HTTP_200_OK)

    def organize_data(self, serialized_data):
        # Implement logic to organize data as needed
        # For example, create a dictionary with names as keys and lists of amounts as values

        organized_data = {}

        for item in serialized_data:
            
            rd_intrest = item.get('rd_interest')
            amount_collected = item['amount_collected']
            collection_date = item['collection_date']
            person_name =item['person_name']
            print(rd_intrest,amount_collected,collection_date,person_name)

            if rd_intrest and amount_collected and collection_date:
                
                formatted_date = collection_date.split('T')[0]
                key = f"{rd_intrest}_{person_name}" 
                print(key)

                if key not in organized_data:
                    organized_data[key] = {}

                if formatted_date not in organized_data[key]:
                    organized_data[key][formatted_date] = 0

                # Accumulate amounts for the same date and person
                organized_data[key][formatted_date] += float(amount_collected)

        return organized_data 
    

class OrignalRDcollectionView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    # without adding collection amount 
    def get(self,request,pk=None,format=None):
        if pk is not None:
            rdintrest = RDColl.objects.filter(rd_interest=pk)
            print(rdintrest)
            serilizer = RDCollectionDataallSerializer(rdintrest,many=True)
            return Response(serilizer.data,status=status.HTTP_200_OK)



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
            loan = LoanInt.objects.get(loan_id=pk) 
            serilizer =  LaonaAmountIntrestSerilizer(loan)
            return Response(serilizer.data,status=status.HTTP_200_OK)
        else:
            loan =LoanInt.objects.all()
            serilizer = LaonaAmountIntrestSerilizer(loan,many=True)
            return Response(serilizer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk=None,format=None):
        loan =  LoanInt.objects.get(loan_id=pk)
        serilizer = LaonaAmountSerilizer(loan,data=request.data) 
        if  serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_200_OK)       
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk=None,format=None):
        loan =  LoanInt.objects.get(loan_id=pk)
        serilizer = LaonaAmountSerilizer(loan,data=request.data) 
        if  serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Loan Updated Successfully','data':serilizer.data},status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)




def merge_by_collection_date_Loan(queryset):
    merged_data = {}
    for item in queryset:
        
        print(item.collection_date)
        collection_date = item.collection_date.date()  # Extract date part
        # print(item.loan_intrest.loan_id)
        loan_intrest_id = item.loan_intrest.loan_id

        if (collection_date, loan_intrest_id) not in merged_data:
            # If entry with same collection date and loan interest does not exist, add it
            merged_data[(collection_date, loan_intrest_id)] = item
        else:
            # If entry with same collection date and loan interest exists, add amount
            merged_data[(collection_date, loan_intrest_id)].amount_collected += item.amount_collected
    
    return merged_data.values()


class LoanCollectionView(APIView):
    renderer_classes =[UserRenderer]
    permission_classes=[IsAuthenticated]
    def post(self,request,format=None):
        serilizer = LoanCollectionSerilizer(data=request.data,many=True)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Loan Intrest Created Successfully','data':serilizer.data},status=status.HTTP_201_CREATED)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,pk=None,format=None):
        if pk is not None:
            loan_collections = LoanColl.objects.filter(loan_intrest=pk)
            merged_data = merge_by_collection_date_Loan(loan_collections)
            serilizer = LoanCollectionDataallSerializer(merged_data,many=True)
            return Response(serilizer.data,status=status.HTTP_200_OK)
        else:   
            rdintrest =LoanColl.objects.all()
            serilizer = LoanCollectionSerilizer(rdintrest,many=True)
            return Response(serilizer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk=None,format=None):
        loan =  LoanColl.objects.get(id=pk)
        serilizer = LoanCollectionSerilizer(loan,data=request.data) 
        if  serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk=None,format=None):
        loan =  LoanColl.objects.get(id=pk)
        serilizer = LoanCollectionSerilizer(loan,data=request.data) 
        if  serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Loancollection Updated Successfully','data':serilizer.data},status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST) 
    



class LoanDataAPIView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        start_date = request.data.get('start_date')  # Format: 'YYYY-MM-DD'
        end_date = request.data.get('end_date')      # Format: 'YYYY-MM-DD'
        start_date_aware = make_aware(datetime.strptime(start_date, '%Y-%m-%d'))
        end_date_aware = make_aware(datetime.strptime(end_date, '%Y-%m-%d'))
        print(start_date_aware, end_date_aware)
        loan_collections = LoanColl.objects.filter(collection_date__range=(start_date_aware, end_date_aware))
        serializer = LoanCollectionDataSerializer(loan_collections, many=True)

        # print(serializer)
        # Organize data as needed
        organized_data = self.organize_data(serializer.data)

        return Response(organized_data, status=status.HTTP_200_OK)

    def organize_data(self, serialized_data):
        # Implement logic to organize data as needed
        # For example, create a dictionary with names as keys and lists of amounts as values

        organized_data = {}

        for item in serialized_data:
            
            loan_intrest = item.get('loan_intrest')
            amount_collected = item['amount_collected']
            collection_date = item['collection_date']
            person_name =item['person_name']

            if loan_intrest and amount_collected and collection_date:
                
                formatted_date = collection_date.split('T')[0]
                key = f"{loan_intrest}_{person_name}" 
                print(key)

                if key not in organized_data:
                    organized_data[key] = {}

                if formatted_date not in organized_data[key]:
                    organized_data[key][formatted_date] = 0

                # Accumulate amounts for the same date and person
                organized_data[key][formatted_date] += float(amount_collected)

        return organized_data 
  
