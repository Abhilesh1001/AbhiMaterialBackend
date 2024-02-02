from collections import defaultdict
import json
from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import GRN,MIR,MaterialIssue
from .serilizer import GRNSerilizer,MiroSerilizer,MaterialIssueSerilizer,POinsertinIRNserilizer
from cusauth.models import User
from cusauth.renderers import UserRenderer
from material.models import PurchaseOrder
from  rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission


def index(request):
    return HttpResponse('ok')



def itemPo(po_no_require):
    grn = GRN.objects.all()
    po = PurchaseOrder.objects.all()

    # Dictionary to store original quantities in PurchaseOrder
    original_po_line = defaultdict(int)

    # Calculate total quantities from PurchaseOrder
    for pureq in po:
        newValPo = json.loads(pureq.item_pr)
        # print('newval',newValPo)
        for item in newValPo:
            po_no = pureq.po_no
            po_line = item["po_line"]
            material_qty = item["material_qty"]
            if material_qty is not None:
                original_po_line[(po_no, po_line)] += int(material_qty)

    remaining_quantities = original_po_line.copy()

    # Calculate remaining quantities by subtracting from GRN
    for purchase in grn:
        newValGrn = json.loads(purchase.item_po)
        
        for item in newValGrn:
            po_no = item["po_no"]
            po_line = item["po_line"]
            material_qty = item["material_qty"]
            if material_qty is not None:
              remaining_quantities[(po_no, po_line)] -= int(material_qty)

    # Create a list of dictionaries for remaining quantities
    remaining_quantities_list = []
    for pureq in po:
        newVal = json.loads(pureq.item_pr)
        if pureq.po_no == po_no_require:
            for item in newVal:
                po_no = pureq.po_no
                po_line = item["po_line"]
                material_qty = remaining_quantities[(po_no, po_line)]
                remaining_dict = {
                    "line_no": item["line_no"],
                    "pr_no": item["pr_no"],
                    "po_line": po_line,
                    "po_no": po_no,
                    "material_no": item['material_no'],
                    "material_name": item["material_name"],
                    "material_unit": item["material_unit"],
                    "material_price": item['material_price'],
                    "material_tax": item["material_tax"],
                    "total_tax": item["total_tax"],
                    "material_qty": material_qty,
                    "total_amount": item["total_amount"],
                    "material_text": item['material_text'],
                }
                remaining_quantities_list.append(remaining_dict)

    return json.dumps(remaining_quantities_list)


class GRNPermission(BasePermission):
    def has_permission(self, request, view):
        required_permissions = [
            'create_grn',
            'post_grn',
            'view_grn',
            'delete_grn',
        ]

        has_all_permissions = all(request.user.has_perm(permission) for permission in required_permissions)
        if not has_all_permissions:
            print(f'User does not have all required permissions: {required_permissions}')


        return has_all_permissions


class GRNView(APIView):
    permission_classes = [IsAuthenticated,GRNPermission]
    renderer_classes = [UserRenderer]
    def post(self,request,format=None):
        serilizer = GRNSerilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Data Created Sucessfully','data':serilizer.data},status=status.HTTP_201_CREATED)
        
        return Response(serilizer.errors)
    
    def get(self,request,pk=None,format=None):
        
        if pk is not None:
            grn = GRN.objects.get(grn_no = pk)
            serilzer =  GRNSerilizer(grn)
            # print(serilzer.data)
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
    
    

def grnoignalpreview(pk):
    grn = GRN.objects.get(grn_no=pk)

    newValgrn = json.loads(grn.item_po)
    grn_avilable_list =[]
    for itemGrn in newValgrn:
        original_qty_po = 0
        original_quantities_json = itemPo(itemGrn["po_no"])
        original_quantities = json.loads(original_quantities_json)
        # print('orignal po',original_quantities)
        for original_item in original_quantities:
            if original_item["po_line"] == itemGrn["po_line"]:
                original_qty_po = original_item["material_qty"]
                # print(original_qty_po)
                break
        remaining_dict = {
            "line_no": itemGrn["line_no"],
            "pr_no": itemGrn["pr_no"],
            "po_line": itemGrn["po_line"],
            "po_no": itemGrn["po_no"],
            "grn_line": itemGrn["grn_line"],
            "material_no": itemGrn['material_no'],
            "material_name": itemGrn["material_name"],
            "material_unit": itemGrn["material_unit"],
            "material_price": itemGrn['material_price'],
            "material_tax": itemGrn["material_tax"],
            "total_tax": itemGrn["total_tax"],
            "material_qty": int(itemGrn["material_qty"]),
            "material_text": itemGrn['material_text'],
            "total_amount": itemGrn["total_amount"],
            "original_qty_po": original_qty_po + int(itemGrn["material_qty"])
            }
        grn_avilable_list.append(remaining_dict)


    return json.dumps(grn_avilable_list) 



class OrGRNView(APIView):
    permission_classes = [IsAuthenticated,GRNPermission]
    renderer_classes = [UserRenderer]

    def get(self,request,pk=None,format=None):
        
        if not request.user.has_perm('view_grn'):
            return Response({'error': 'You do not have permission to view GRN.'}, status=status.HTTP_403_FORBIDDEN)
         
        if pk is not None:
            grn = GRN.objects.get(grn_no = pk)           
            grn_item = {"user" : grn.user,"time":grn.time,"item_po":grnoignalpreview(pk),"vendor_address":grn.vendor_address,"delivery_address":grn.delivery_address,"maindata":grn.maindata,"billing":grn.billing,"grn_no":pk}
            serilzer =  GRNSerilizer(grn_item)
            # print(serilzer.data)
            return Response(serilzer.data,status=status.HTTP_200_OK)
        else:
            grn = GRN.objects.all()
            serilzer =GRNSerilizer(grn,many=True)
            return Response(serilzer.data,status=status.HTTP_200_OK)
        
class MiroView(APIView):
    permission_classes =[IsAuthenticated]
    renderer_classes= [UserRenderer]

    def post(self,request,format=None):
        serilizer = MiroSerilizer(data=request.data) 
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Data created SuccessFully','data':serilizer.data},status=status.HTTP_201_CREATED)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk=None,format=None):
        if pk is not None:
            miro =  MIR.objects.get(mir_no=pk)
            serillizer = MiroSerilizer(miro)
            return (serillizer.data)
        else:
            miro = MIR.objects.all()
            serillizer = MiroSerilizer(miro,many=True)
            return (serillizer.data)
    
    def patch(self,request,pk=None,format=None):
        miro = MIR.objects.get(mir_no=pk)
        serilizer =  MiroSerilizer(miro,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Data Updated Sussfully','data':serilizer.data},status=status.HTTP_200_OK)
          
        
class MaterialIssueView(APIView):
    permission_classes =[IsAuthenticated]
    renderer_classes= [UserRenderer]

    def post(self,request,format=None):
        serilizer = MaterialIssueSerilizer(data=request.data) 
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Data created SuccessFully','data':serilizer.data},status=status.HTTP_201_CREATED)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk=None,format=None):
        if pk is not None:
            miro =  MIR.objects.get(mir_no=pk)
            serillizer = MaterialIssueSerilizer(miro)
            return (serillizer.data)
        else:
            miro = MIR.objects.all()
            serillizer = MaterialIssueSerilizer(miro,many=True)
            return (serillizer.data)
    
    def patch(self,request,pk=None,format=None):
        miro = MIR.objects.get(mir_no=pk)
        serilizer =  MaterialIssueSerilizer(miro,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Data Updated Sussfully','data':serilizer.data},status=status.HTTP_200_OK)

            

class POinINRView(APIView):

    def get(self,request,pk=None,format=None):
        grn = GRN.objects.all()
        pono = PurchaseOrder.objects.get(pk=pk)
        
        dicttonery = []
        for po in grn:
            item_po =  json.loads(po.item_po)
            dict = {}
            for item in item_po:
                if int(item['po_no']) is pk:
                    dict = {
                        "line_no" : item["line_no"],
                        "pr_no": item["pr_no"],
                        "po_line":item["po_line"],
                        "po_no":item["po_no"],
                        "grn_line":item["grn_line"],
                        'grn_no':po.grn_no,
                        "material_no":item["material_no"],
                        'material_name':item["material_name"],
                        'material_unit':item["material_unit"],
                        'material_price':item["material_price"],
                        'material_tax':float(item["material_tax"]),
                        'total_tax':item["total_tax"],
                        'material_qty':item["material_qty"],
                        'material_text':item["material_text"],
                        'total_amount':item["total_amount"],
                        'billing':po.billing
                    }
                    dicttonery.append(dict)
        newPoforIRN = json.dumps(dicttonery)
        # print(newPoforIRN)
        poreturn = {"po_no":pono.po_no,"user":pono.user,'time':pono.time,"vendor_address":pono.vendor_address,'delivery_address':pono.delivery_address,'item_pr':newPoforIRN}
        serilizer = POinsertinIRNserilizer(poreturn)
       
        return Response(serilizer.data)
