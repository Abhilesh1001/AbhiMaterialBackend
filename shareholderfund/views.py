from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serilizer import ShareHolderFunsSerilizer,ShareHolderNameSerilizer,SerilzerHOlderFund,RDCollectionSerializer,RDCollectionDataSerializer,PersonSerializer,LoanCollectionDataSerializer,LoanCollectionSerializer,LoanPersonSerializer,LaonaAmountSerilizer,ShareHolderFunsDataDisSerializer,RDCollectionSerializerData,LoanCollectionSerilizerData,RdIntersetSerilizer,RdIntersetOrignalSerilizer,RDColloectionNewSerilizer,RDCollectionNewDataSerializer,RDCollectionNewDataallSerializer,LaonaAmountIntrestSerilizer,LoanCollectionNewSerilizer,LoanCollectionNewDataallSerializer,LoanCollectionNewDataSerializer
from .models import ShareHolderFuns,ShareHolderName,RdPerson,RDCollection,LoanCollection,LoanPerson,LoanAmount,RDCollectionNew,RDIntrest,LoanCollectionNew
from rest_framework.permissions import IsAuthenticated
from cusauth.renderers import UserRenderer
import json



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
            return Response({'msg':'Data creates Successfully'},status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors)
        
    def get(self,request,pk=None,format=None):

        if pk is not None:
            # get all data of pk person 
            
            sh = ShareHolderFuns.objects.filter(sh_name=pk)
            
            dict =  []
            for item in sh:
                print(item.amount_Debit)
                dict1= {
                    "name ":item.sh_name.name,
                    "shf_id":item.shf_id,
                    "Sh_id":item.sh_name.Sh_id,
                    "amount_credit":item.amount_credit,
                    "amount_Debit":item.amount_Debit,
                    "time":item.time
                }

                dict.append(dict1)
            print(dict)

            serilizer =  ShareHolderFunsDataDisSerializer(sh,many=True)
            
            
            return Response(serilizer.data,status=status.HTTP_200_OK)
        else:
            sh = ShareHolderFuns.objects.all()
            serilizer =  ShareHolderFunsDataDisSerializer(sh,many= True)

            return Response(serilizer.data,status=status.HTTP_200_OK)


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
        sh = ShareHolderName.objects.get(Sh_id=pk)
        print(sh)
        serilizer = ShareHolderNameSerilizer(sh,data=request.data)
        if  serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Holder Updated Successfully','data':serilizer.data},status=status.HTTP_200_OK)
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
            rd_personcoll_data = RDCollection.objects.filter(person=pk)
            serializer = RDCollectionSerializerData(rd_personcoll_data, many=True)

            return Response(serializer.data)
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
            return Response({'msg':'Rd person Updated Successfully','data':serilizer.data},status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)



from django.utils.timezone import make_aware
from datetime import datetime
class RDDataAPIView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        start_date = request.data.get('start_date')  # Format: 'YYYY-MM-DD'
        end_date = request.data.get('end_date')      # Format: 'YYYY-MM-DD'
        print(start_date,end_date)
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
            loan_perperson = LoanCollection.objects.filter(loan_person=pk)
            serializer = LoanCollectionSerilizerData(loan_perperson, many=True)
            return Response(serializer.data)
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
            return Response({'msg':'Loan Person Updated Successfully','data':serilizer.data},status=status.HTTP_200_OK)
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
            serilizer =  LaonaAmountIntrestSerilizer(loan)
            return Response(serilizer.data,status=status.HTTP_200_OK)
        else:
            loan =LoanAmount.objects.all()
            serilizer = LaonaAmountIntrestSerilizer(loan,many=True)
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
            return Response({'msg':'Loan Updated Successfully','data':serilizer.data},status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

    

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
            rdintrest = RDIntrest.objects.get(rd_intrest_id=pk) 
            serilizer = RdIntersetSerilizer(rdintrest)
            return Response(serilizer.data,status=status.HTTP_200_OK)
        else:
            rdintrest =RDIntrest.objects.all()
            serilizer = RdIntersetSerilizer(rdintrest,many=True)
            return Response(serilizer.data,status=status.HTTP_200_OK)
        
    def put(self,request,pk=None,format=None):
        loan =  RDIntrest.objects.get(rd_intrest_id=pk)
        serilizer = RdIntersetOrignalSerilizer(loan,data=request.data) 
        if  serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk=None,format=None):
        loan =  RDIntrest.objects.get(rd_intrest_id=pk)
        print(loan)
        serilizer = RdIntersetOrignalSerilizer(loan,data=request.data) 
        if  serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'RDIntrest Updated Successfully','data':serilizer.data},status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)




def merge_by_collection_date(queryset):
        merged_data = {}
        for item in queryset:
            collection_date = item.collection_date.date()  # Extract date part
            rd_intrest_id = item.rd_intrest.rd_intrest_id
            if (collection_date, rd_intrest_id) not in merged_data:
                merged_data[(collection_date, rd_intrest_id)] = item
            else:
                # If entry with same collection date and rd_intrest exists, add amount
                merged_data[(collection_date, rd_intrest_id)].amount_collected +=item.amount_collected
        return merged_data.values()


class RDcollectionNewView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):
        serilizer = RDColloectionNewSerilizer(data=request.data,many=True)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'RD Intrest Created Successfully','data':serilizer.data},status=status.HTTP_201_CREATED)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,pk=None,format=None):
        if pk is not None:
            rd_collections = RDCollectionNew.objects.filter(rd_intrest=pk)
            merged_data = merge_by_collection_date(rd_collections)
            serilizer = RDCollectionNewDataallSerializer(merged_data,many=True)
            return Response(serilizer.data,status=status.HTTP_200_OK)
        else:   
            rdintrest =RDCollectionNew.objects.all()
            serilizer = RDColloectionNewSerilizer(rdintrest,many=True)
            return Response(serilizer.data,status=status.HTTP_200_OK)
        
    def put(self,request,pk=None,format=None):
        loan =  RDCollectionNew.objects.get(rd_intrest_id=pk)
        serilizer = RDColloectionNewSerilizer(loan,data=request.data) 
        if  serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk=None,format=None):
        loan =  RDCollectionNew.objects.get(rd_intrest_id=pk)
        serilizer = RDColloectionNewSerilizer(loan,data=request.data) 
        if  serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'RDcollection Updated Successfully','data':serilizer.data},status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)




class RDDataNewAPIView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        start_date = request.data.get('start_date')  # Format: 'YYYY-MM-DD'
        end_date = request.data.get('end_date')      # Format: 'YYYY-MM-DD'
        start_date_aware = make_aware(datetime.strptime(start_date, '%Y-%m-%d'))
        end_date_aware = make_aware(datetime.strptime(end_date, '%Y-%m-%d'))
        print(start_date_aware, end_date_aware)
        rd_collections = RDCollectionNew.objects.filter(collection_date__range=(start_date_aware, end_date_aware))
        serializer = RDCollectionNewDataSerializer(rd_collections, many=True)

        # print(serializer)
        # Organize data as needed
        organized_data = self.organize_data(serializer.data)

        return Response(organized_data, status=status.HTTP_200_OK)

    def organize_data(self, serialized_data):
        # Implement logic to organize data as needed
        # For example, create a dictionary with names as keys and lists of amounts as values

        organized_data = {}

        for item in serialized_data:
            
            rd_intrest = item.get('rd_intrest')
            amount_collected = item['amount_collected']
            collection_date = item['collection_date']
            person_name =item['person_name']

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
    


class OrignalRDcollectionNewView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    # without adding collection amount 
    def get(self,request,pk=None,format=None):
        if pk is not None:
            rdintrest = RDCollectionNew.objects.filter(rd_intrest=pk)
            print(rdintrest)
            serilizer = RDCollectionNewDataallSerializer(rdintrest,many=True)
            return Response(serilizer.data,status=status.HTTP_200_OK)



def merge_by_collection_date_Loan(queryset):
    merged_data = {}
    for item in queryset:
        
        print(item.collection_date)
        collection_date = item.collection_date.date()  # Extract date part
        loan_intrest_id = item.loan_intrest.id

        if (collection_date, loan_intrest_id) not in merged_data:
            # If entry with same collection date and loan interest does not exist, add it
            merged_data[(collection_date, loan_intrest_id)] = item
        else:
            # If entry with same collection date and loan interest exists, add amount
            merged_data[(collection_date, loan_intrest_id)].amount_collected += item.amount_collected
    
    return merged_data.values()


class LoanCollectionNewView(APIView):
    renderer_classes =[UserRenderer]
    permission_classes=[IsAuthenticated]
    def post(self,request,format=None):
        serilizer = LoanCollectionNewSerilizer(data=request.data,many=True)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Loan Intrest Created Successfully','data':serilizer.data},status=status.HTTP_201_CREATED)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,pk=None,format=None):
        if pk is not None:
            loan_collections = LoanCollectionNew.objects.filter(loan_intrest=pk)
            merged_data = merge_by_collection_date_Loan(loan_collections)
            serilizer = LoanCollectionNewDataallSerializer(merged_data,many=True)
            return Response(serilizer.data,status=status.HTTP_200_OK)
        else:   
            rdintrest =LoanCollectionNew.objects.all()
            serilizer = LoanCollectionNewSerilizer(rdintrest,many=True)
            return Response(serilizer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk=None,format=None):
        loan =  LoanCollectionNew.objects.get(id=pk)
        serilizer = LoanCollectionNewSerilizer(loan,data=request.data) 
        if  serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk=None,format=None):
        loan =  LoanCollectionNew.objects.get(id=pk)
        serilizer = LoanCollectionNewSerilizer(loan,data=request.data) 
        if  serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Loancollection Updated Successfully','data':serilizer.data},status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST) 
    


class LoanDataNewAPIView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        start_date = request.data.get('start_date')  # Format: 'YYYY-MM-DD'
        end_date = request.data.get('end_date')      # Format: 'YYYY-MM-DD'
        start_date_aware = make_aware(datetime.strptime(start_date, '%Y-%m-%d'))
        end_date_aware = make_aware(datetime.strptime(end_date, '%Y-%m-%d'))
        print(start_date_aware, end_date_aware)
        loan_collections = LoanCollectionNew.objects.filter(collection_date__range=(start_date_aware, end_date_aware))
        serializer = LoanCollectionNewDataSerializer(loan_collections, many=True)

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
  

class OrignalLoancollectionNewView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    # without adding collection amount 
    def get(self,request,pk=None,format=None):
        if pk is not None:
            loanintrest = RDCollectionNew.objects.filter(loan_intrest=pk)
            print(loanintrest)
            serilizer = LoanCollectionNewDataallSerializer(loanintrest,many=True)
            return Response(serilizer.data,status=status.HTTP_200_OK)



            

