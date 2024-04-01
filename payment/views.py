from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from .serilizer import AdvancePaymentsErilizer,PaymentsErilizer,AdvancePaymentsSerilizerChange,PaymentSerilizerAll
from rest_framework.response import Response
from rest_framework import status
from .models import AdvancePayment,PaymentTovendor
from material.models import PurchaseOrder
from rest_framework.permissions import IsAuthenticated
from cusauth.renderers import UserRenderer

# Create your views here.
def index(request):
    return HttpResponse('Payment Page')

class AdvancePaymaentView(APIView):

    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):
        serilizer = AdvancePaymentsErilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Advance Payment created successfully','data':serilizer.data},status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors) 
    
    def get(self,request,pk=None,format=None):
        if pk is not None:
            advancepayment =  AdvancePayment.objects.get(advance_payment_no=pk)

            serilizer =  AdvancePaymentsSerilizerChange(advancepayment)

            return Response(serilizer.data,status=status.HTTP_200_OK)
        else:
            advancepayment =  AdvancePayment.objects.all()
            serilizer = AdvancePaymentsSerilizerChange(advancepayment,many=True)
            return Response(serilizer.data,status=status.HTTP_200_OK)

    def put(self,request,pk=None,format=None):
        advancepayment = AdvancePayment.objects.get(advance_payment_no=pk)
        serilizer = AdvancePaymentsErilizer(advancepayment,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Data change successfully'},status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self,request,pk=None,format=None):
        
        advancepayment = AdvancePayment.objects.get(advance_payment_no=pk)
        print(pk)
        serilizer = AdvancePaymentsErilizer(advancepayment,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Data change successfully','data':serilizer.data},status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
        


class PaymaentView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):
        serilizer = PaymentsErilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Payment done successfully','data':serilizer.data},status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors) 
    
    def get(self,request,pk=None,format=None):
        if pk is not None:
            
            payment =  PaymentTovendor.objects.get(payment_no=pk)
            serilizer =  PaymentsErilizer(payment)
            return Response(serilizer.data,status=status.HTTP_200_OK)
        else:
            payment =  PaymentTovendor.objects.all()
            serilizer = PaymentSerilizerAll(payment,many=True)
            return Response(serilizer.data,status=status.HTTP_200_OK)

    def put(self,request,pk=None,format=None):
        payment = PaymentTovendor.objects.get(payment_no=pk)
        serilizer = PaymentsErilizer(payment,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Data change successfully'},status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self,request,pk=None,format=None):
        payment = PaymentTovendor.objects.get(payment_no=pk)
        serilizer = PaymentsErilizer(payment,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'data change successfully','data':serilizer.data},status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
        

from collections import defaultdict

class PaymentFilterByMiro(APIView):
    def get(self,request,pk=None,format=None):
        if pk is not None:
            
            payment =  PaymentTovendor.objects.get(payment_no=pk)
            serilizer =  PaymentsErilizer(payment)
            return Response(serilizer.data,status=status.HTTP_200_OK)
        else:
            payment =  PaymentTovendor.objects.all()
            serilizer = PaymentSerilizerAll(payment,many=True)
            accumulated_amounts = defaultdict(float)
            for payment in serilizer.data:
                miro_no = payment['miro_no']
                advance_adjust = float(payment['advance_adjust'])
                amount_debit = float(payment['amount_debit'])                
                # Subtract amount_debit if the miro_no already exists
                accumulated_amounts[miro_no] += amount_debit - advance_adjust
            # print(accumulated_amounts)
            newDict = []
            for miro_no, accumulated_amount in accumulated_amounts.items():
                for item in serilizer.data:
                    print(item['miro_no'], miro_no)
                    if item['miro_no'] == miro_no:
                        dict ={
                            "miro_no" :  miro_no,
                            "main_data" : item["main_data"],
                            "bill_no" : item["bill_no"],
                            "total_paid_amount" :accumulated_amount,
                            "vendor_name" :  item["vendor_name"],
                            "item_grn" :  item["item_grn"]
                        }
                        newDict.append(dict)    
                        break
            
                    
            return Response(newDict,status=status.HTTP_200_OK)


