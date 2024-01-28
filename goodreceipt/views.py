from collections import defaultdict
import json
from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import GRN
from .serilizer import GRNSerilizer
from cusauth.models import User
from cusauth.renderers import UserRenderer
from material.models import PurchaseOrder
from  rest_framework.permissions import IsAuthenticated

# Create your views here.

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
        for original_item in original_quantities:
            if original_item["po_line"] == itemGrn["po_line"]:
                original_qty_po = original_item["material_qty"]
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
            "original_qty_po": original_qty_po 
            }
        grn_avilable_list.append(remaining_dict)


    return json.dumps(grn_avilable_list) 




class OrGRNView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]

    def get(self,request,pk=None,format=None):
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

