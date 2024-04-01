from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from .serilizer import AdvancePaymentsErilizer,PaymentsErilizer,AdvancePaymentsSerilizerChange,PaymentSerilizerAll,MiroSerilizer
from rest_framework.response import Response
from rest_framework import status
from .models import AdvancePayment,PaymentTovendor
from material.models import PurchaseOrder
from rest_framework.permissions import IsAuthenticated
from cusauth.renderers import UserRenderer
import json
from goodreceipt.models import MIR

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
            return Response({'msg':'Data change successfully','data':serilizer.data},status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
        

from collections import defaultdict

class PaymentFilterByMiro(APIView):
    renderer_classes = [UserRenderer]
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
                accumulated_amounts[miro_no] += amount_debit + advance_adjust
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

class MiroPaymentView(APIView):
    def get(self,request,pk=None,format=None):
        paymenttovendor = MIR.objects.filter(mir_no=pk)
        paymettovendor = PaymentTovendor.objects.filter(miro_no=pk)
        total_advance = 0
        for item in paymenttovendor:
            json_data = json.loads(item.item_grn)
            po_no = json_data[0]['po_no']
            total_advance_payment =  AdvancePayment.objects.filter(po_no=po_no)
            for items in total_advance_payment:
                total_advance+=items.amount_debit 
            break
        totaladvanceadjust = 0
        for items in paymettovendor:
            print(items)
            totaladvanceadjust += items.advance_adjust 
        balance_amount = total_advance - totaladvanceadjust 

        miro = MIR.objects.get(mir_no=pk)
        serilizer = MiroSerilizer(miro)  


        total_paymant =0 
        payment =  PaymentTovendor.objects.filter(miro_no=pk)
        for item in payment:
            print(item.amount_debit)
            total_paymant +=item.amount_debit + item.advance_adjust
        
        return Response({'data':serilizer.data,"total_advance_balance":balance_amount,'total_paymet':total_paymant  })
    



class PaymentUpdateView(APIView):
    def get(self,request,pk=None,format=None):
        paymettovendor = PaymentTovendor.objects.get(payment_no=pk)
        miro_no = paymettovendor.miro_no.mir_no
        # print(miro_no)
        paymenttovendor = MIR.objects.filter(mir_no=miro_no)
        print(paymenttovendor,'.........')

        total_advance = 0
        for item in paymenttovendor:
            json_data = json.loads(item.item_grn)
            po_no = json_data[0]['po_no']
            total_advance_payment =  AdvancePayment.objects.filter(po_no=po_no)
            for items in total_advance_payment:
                total_advance+=items.amount_debit 
            break
        totaladvanceadjust = 0

        allpayvendormrn = PaymentTovendor.objects.filter(miro_no=miro_no)

        for items in allpayvendormrn:
            print(items)
            totaladvanceadjust += items.advance_adjust 
        balance_amount = total_advance - totaladvanceadjust 


        miro = MIR.objects.get(mir_no=miro_no)
        serilizer = MiroSerilizer(miro)  

        total_paymant =0 

        payment =  PaymentTovendor.objects.filter(miro_no=miro_no) 
        for item in payment:
            print(item.amount_debit)
            total_paymant +=item.amount_debit + item.advance_adjust

        newata  = {'data':serilizer.data,"total_advance_balance":balance_amount,'total_paymet':total_paymant  }
        
        return Response(newata)