from django.shortcuts import render,HttpResponse
from . models import Material,PurchaseRequestNew,Vendor,DeliveryAdress,PurchaseOrder
from cusauth.models import User 
from cusauth.renderers import UserRenderer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serlilizer import MaterialSerlizer,PurchaseRequestSerializer,VendorSErilizer,DeliverySerilizer,PurchaseOrderSerilizer
from rest_framework.response import Response
from rest_framework import status 
import json
from collections import defaultdict
from goodreceipt.models import GRN


#Absolute View 
def index1(request):
    po = PurchaseOrder.objects.all()
    pr = PurchaseRequestNew.objects.all()
    # print(pr)
    orignal_pr_line = defaultdict(int)
    for pureq in pr:
        # print('pr',pureq.user)
        newVal=  json.loads(pureq.item_json)
        for item in newVal:
            pr_no = pureq.pr_no
            line_no = item["line_no"]
            material_quantity = item["material_qty"]
            # print(line_no,type(material_quantity))
            orignal_pr_line[(pr_no, line_no)] += int(material_quantity)

    for (pr_no, line_no), total_quantity in orignal_pr_line.items():
        print(f"PR orignal No: {pr_no}, Line No: {line_no}, Total Quantity: {total_quantity}")

    # po view 
    pr_line_totals = defaultdict(int)
    for purchase in po:
        # print('purchase',json.loads(purchase.item_pr))
        newVal = json.loads(purchase.item_pr)
        for item in newVal:
            pr_no = item["pr_no"]
            line_no = item["line_no"]
            material_quantity = item["material_qty"]
            # print(line_no,type(material_quantity))
            pr_line_totals[(pr_no, line_no)] += int(material_quantity)

    print('Total Avilabel in PO',pr_line_totals)     
    for (pr_no, line_no), total_quantity in pr_line_totals.items():
        print(f"PR poview No: {pr_no}, Line No: {line_no}, Total Quantity: {total_quantity}")

    # avalible quantity 
        
    # from here remaning quantity calculation 
    original_pr_line = defaultdict(int)
    for pureq in pr:
        newVal = json.loads(pureq.item_json)
        for item in newVal:
            pr_no = pureq.pr_no
            line_no = item["line_no"]
            material_qty = item["material_qty"]
            # print(line_no,type(material_quantity))
            original_pr_line[(pr_no, line_no)] += int(material_qty)

    # Print total quantities in PurchaseRequestNew
    for (pr_no, line_no), total_quantity in original_pr_line.items():
        print(f"PR original No: {pr_no}, Line No: {line_no}, Total Quantity: {total_quantity}")


    remaining_quantities = original_pr_line.copy()  
    for purchase in po:
        newVal = json.loads(purchase.item_pr)
        for item in newVal:
            pr_no = item["pr_no"]
            line_no = item["line_no"]
            material_qty = item["material_qty"]

            # print(line_no,type(material_quantity))
            remaining_quantities[(pr_no, line_no)] -= int(material_qty)
   
    # Print remaining quantities after deduction from PurchaseOrder
    for (pr_no, line_no), remaining_quantity in remaining_quantities.items():
        print(f"PR remaining No: {pr_no}, Line No: {line_no}, Remaining Quantity: {remaining_quantity}")

    # Third Approach 
    remaining_quantities_list = []
    for purchase in po:
        newVal = json.loads(purchase.item_pr)
        for item in newVal:
            pr_no = item["pr_no"]
            line_no = item["line_no"]
            material_quantity = item["material_qty"]
            remaining_quantities_list[(pr_no, line_no)] -= int(material_quantity)
            print()
            # Create dictionary for remaining quantities
            remaining_dict = {
                "pr_no": pr_no,
                "line_no": line_no,
                "material_qty": remaining_quantities[(pr_no, line_no)]
            }
            remaining_quantities_list.append(remaining_dict)

    # Print list of dictionaries for remaining quantities
    print(remaining_quantities_list)

    return HttpResponse('hello froends')

#Absolute View 
def index2(request):
    po = PurchaseOrder.objects.all()
    pr = PurchaseRequestNew.objects.all()

    # Dictionary to store original quantities in PurchaseRequestNew
    original_pr_line = defaultdict(int)

    # Calculate total quantities from PurchaseRequestNew
    for pureq in pr:
        newVal = json.loads(pureq.item_json)
        for item in newVal:
            pr_no = pureq.pr_no
            line_no = item["line_no"]
            material_qty = item["material_qty"]
            original_pr_line[(pr_no, line_no)] += material_qty

    # Print total quantities in PurchaseRequestNew
    for (pr_no, line_no), total_quantity in original_pr_line.items():
        print(f"PR original No: {pr_no}, Line No: {line_no}, Total Quantity: {total_quantity}")

    # Dictionary to store remaining quantities after deducting from PurchaseOrder
    remaining_quantities = original_pr_line.copy()

    # Calculate remaining quantities by subtracting from PurchaseOrder
    for purchase in po:
        newVal = json.loads(purchase.item_pr)
        # print(newVal)
        for item in newVal:
            pr_no = item["pr_no"]
            line_no = item["line_no"]
            material_qty = item["material_qty"]
            remaining_quantities[(pr_no, line_no)] -= int(material_qty)

    # Create a list of dictionaries for remaining quantities
    remaining_quantities_list = []
    for (pr_no, line_no), material_qty in remaining_quantities.items():
        remaining_dict = {
            "pr_no": pr_no,
            "line_no": line_no,
            "material_qty": material_qty,
            # Add other items here if needed
        }
        remaining_quantities_list.append(remaining_dict)

    # Print list of dictionaries for remaining quantities
    print(remaining_quantities_list)

    return HttpResponse('hello friends')

from collections import defaultdict

#Absolute View 
def index(request):
    po = PurchaseOrder.objects.all()
    pr = PurchaseRequestNew.objects.all()

    # Dictionary to store original quantities in PurchaseRequestNew
    original_pr_line = defaultdict(int)

    # Calculate total quantities from PurchaseRequestNew
    for pureq in pr:
        newVal = json.loads(pureq.item_json)
        for item in newVal:
            pr_no = pureq.pr_no
            line_no = item["line_no"]
            material_qty = item["material_qty"]
            original_pr_line[(pr_no, line_no)] += material_qty

    # Print total quantities in PurchaseRequestNew
    for (pr_no, line_no), total_quantity in original_pr_line.items():
        print(f"PR original No: {pr_no}, Line No: {line_no}, Total Quantity: {total_quantity}")

    # Dictionary to store remaining quantities after deducting from PurchaseOrder
    remaining_quantities = original_pr_line.copy()

    # Calculate remaining quantities by subtracting from PurchaseOrder
    for purchase in po:
        newVal = json.loads(purchase.item_pr)
        for item in newVal:
            pr_no = item["pr_no"]
            line_no = item["line_no"]
            material_qty = item["material_qty"]
            remaining_quantities[(pr_no, line_no)] -= int(material_qty)

    # Create a list of dictionaries for remaining quantities
    remaining_quantities_list = []
    for pureq in pr:
        newVal = json.loads(pureq.item_json)
        print(newVal)
        for item in newVal:
            pr_no = pureq.pr_no
            line_no = item["line_no"]
            material_qty = remaining_quantities[(pr_no, line_no)]
            remaining_dict = {
                "pr_no": pr_no,
                "line_no": line_no,
                "material_no":item['material_no'],
                "material_name" : item["material_name"],
                "material_unit":item["material_unit"],
                "material_price" :item['material_price'],
                "material_qty": material_qty,
                "total_price":item["total_price"],
                "material_text" :item['material_text'],
                # Add other items here if needed
            }
            remaining_quantities_list.append(remaining_dict)

    # Print list of dictionaries for remaining quantities
    print(remaining_quantities_list)

    return HttpResponse('hello friends')


def itemPr(pr_no_require):
    po = PurchaseOrder.objects.all()
    pr = PurchaseRequestNew.objects.all()

    # Dictionary to store original quantities in PurchaseRequestNew
    original_pr_line = defaultdict(int)

    # Calculate total quantities from PurchaseRequestNew
    for pureq in pr:
        newValPr = json.loads(pureq.item_json)

        for item in newValPr:
            pr_no = pureq.pr_no
            line_no = item["line_no"]
            material_qty = item["material_qty"]
            if material_qty is not None:
                original_pr_line[(pr_no, line_no)] += int(material_qty)

    remaining_quantities = original_pr_line.copy()

    # Calculate remaining quantities by subtracting from PurchaseOrder
    for purchase in po:
        newValPo = json.loads(purchase.item_pr)
        
        for item in newValPo:
            # print(item)
            pr_no = item["pr_no"]
            line_no = item["line_no"]
            material_qty = item["material_qty"]
            if material_qty is not None:
              remaining_quantities[(pr_no, line_no)] -= int(material_qty)

    # Create a list of dictionaries for remaining quantities
    remaining_quantities_list = []
    for pureq in pr:
        newVal = json.loads(pureq.item_json)
        # print(newVal)
        if pureq.pr_no is pr_no_require:
            for item in newVal:
                pr_no = pureq.pr_no
                line_no = item["line_no"]
                material_qty = remaining_quantities[(pr_no, line_no)]
                remaining_dict = {
                    "pr_no": pr_no,
                    "line_no": line_no,
                    "material_no":item['material_no'],
                    "material_name" : item["material_name"],
                    "material_unit":item["material_unit"],
                    "material_price" :item['material_price'],
                    "material_qty": material_qty,
                    "total_price":item["total_price"],
                    "material_text" :item['material_text'],

                }
                remaining_quantities_list.append(remaining_dict)

    return json.dumps(remaining_quantities_list)

class MaterialView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]
    def post(self,request,format=None):
        serilizer = MaterialSerlizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'data created successfully','data':serilizer.data})
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk=None,format=None):

        if pk is None:
            mat = Material.objects.all()
            serilizer = MaterialSerlizer(mat,many =True)
            return Response(serilizer.data,status=status.HTTP_200_OK)
        else:
            pro = Material.objects.get(s_no=pk) 
            serilizer = MaterialSerlizer(pro)
            return Response(serilizer.data)

    
    
    def put(self,request,pk=None,format=None):
        mat = Material.objects.get(pk=pk)
        # print(mat)
        serilizer = MaterialSerlizer(mat,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk=None,format=None):
        mat = Material.objects.get(pk=pk)
        serilizer = MaterialSerlizer(mat,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class PurchaseRequestNewView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        if pk is not None:
            pr = PurchaseRequestNew.objects.get(pr_no=pk)
            # print('print',itemPr(pk),pr.user)
            pr_new = {"user" : pr.user,"time":pr.time,"item_json":itemPr(pk)}
            serializer = PurchaseRequestSerializer(pr_new)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            pr = PurchaseRequestNew.objects.all()
            serializer = PurchaseRequestSerializer(pr, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = PurchaseRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data saved successfully','data':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        pr = PurchaseRequestNew.objects.get(pr_no=pk)
        serializer = PurchaseRequestSerializer(pr, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data changed successfully','data':serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, format=None):
        pr = PurchaseRequestNew.objects.get(pr_no=pk)
        serializer = PurchaseRequestSerializer(pr, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data changed successfully','data':serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serilizer = VendorSErilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Data created Successfully'},status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request,format=None):
        vendor = Vendor.objects.all()
        serilizer = VendorSErilizer(vendor,many=True)
        return Response(serilizer.data)
    
    def get(self,request,pk=None,format=None):
        vendor = Vendor.objects.get(s_no=pk)
        serilizer = VendorSErilizer(vendor)
        return Response(serilizer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk=None,format=None):
        vendor = Vendor.objects.get(s_no=pk)
        serilizer = VendorSErilizer(vendor,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'data change successfully'},status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk=None,format=None):
        vendor = Vendor.objects.get(s_no=pk)
        serilizer = VendorSErilizer(vendor,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'data change successfully'},status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class DeliveryAdressView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serilizer = DeliverySerilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Data created Successfully'},status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request,format=None):
        vendor = DeliveryAdress.objects.all()
        serilizer = DeliverySerilizer(vendor,many=True)
        return Response(serilizer.data)
    
    def get(self,request,pk=None,format=None):
        vendor = DeliveryAdress.objects.get(s_no=pk)
        serilizer = DeliverySerilizer(vendor)
        return Response(serilizer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk=None,format=None):
        vendor = DeliveryAdress.objects.get(s_no=pk)
        serilizer = DeliverySerilizer(vendor,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'data change successfully'},status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk=None,format=None):
        vendor = DeliveryAdress.objects.get(s_no=pk)
        serilizer = DeliverySerilizer(vendor,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'data change successfully'},status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    


# remaning po view for GRN 
def itemPo(po_no_require):
    grn = GRN.objects.all()
    po = PurchaseOrder.objects.all()

    # Dictionary to store original quantities in PurchaseRequestNew
    original_po_line = defaultdict(int)

    # Calculate total quantities from PurchaseRequestNew
    for pureq in po:
        newValPo = json.loads(pureq.item_pr)

        for item in newValPo:
            po_no = pureq.po_no
            po_line = item["po_line"]
            material_qty = item["material_qty"]
            if material_qty is not None:
                original_po_line[(po_no, po_line)] += int(material_qty)

    remaining_quantities = original_po_line.copy()

    # Calculate remaining quantities by subtracting from PurchaseOrder
    for purchase in grn:
        newValPo = json.loads(purchase.item_po)
        
        for item in newValPo:
            # print(item)
            po_no = item["po_no"]
            po_line = item["po_line"]
            material_qty = item["material_qty"]
            if material_qty is not None:
              remaining_quantities[(po_no, po_line)] -= int(material_qty)

    # Create a list of dictionaries for remaining quantities
    remaining_quantities_list = []
    for pureq in po:
        newVal = json.loads(pureq.item_pr)
        # print(newVal)
        if pureq.po_no is po_no_require:
            for item in newVal:
                po_no = pureq.po_no
                po_line = item["po_line"]
                material_qty = remaining_quantities[(po_no, po_line)]
                remaining_dict = {
                    "line_no": item["line_no"],
                    "pr_no": item["pr_no"],
                     "po_line":po_line,
                     "po_no":po_no,
                    "material_no":item['material_no'],
                    "material_name" : item["material_name"],
                    "material_unit":item["material_unit"],
                    "material_price" :item['material_price'],
                    "material_tax":item["material_tax"],
                    "total_tax" :item["total_tax"],
                    "material_qty": material_qty,
                    "total_amount":item["total_amount"],
                    "material_text" :item['material_text'],
                    

                }
                remaining_quantities_list.append(remaining_dict)
        
    
    return json.dumps(remaining_quantities_list)



class PurchaseOrderView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serilizer = PurchaseOrderSerilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'data created successfully','data':serilizer.data})
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST) 

    def get(self,request,pk=None,format=None):
        
        if pk is not None:
            po = PurchaseOrder.objects.get(po_no=pk)
            po_item = {"user" : po.user,"time":po.time,"item_pr":itemPo(pk),"vendor_address":po.vendor_address,"delivery_address":po.delivery_address,"maindata":po.maindata}
            serilizer = PurchaseOrderSerilizer(po_item)
            
            return Response(serilizer.data,status=status.HTTP_200_OK)
        else:
             po = PurchaseOrder.objects.all()
             serilizer = PurchaseOrderSerilizer(po,many=True)
             return Response(serilizer.data,status=status.HTTP_200_OK)
        
    def put(self,request,pk=None,format=None):
        po = PurchaseOrder.objects.get(po_no=pk)
        serilizer = PurchaseOrderSerilizer(po,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'data change successfully'},status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk=None,format=None):
        po = PurchaseOrder.objects.get(po_no=pk)
        serilizer = PurchaseOrderSerilizer(po,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'data change successfully','data':serilizer.data},status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)






from collections import defaultdict
import json
# orignal pr with no change if po created 
def prignalprpreview(pk):
    pr = PurchaseRequestNew.objects.get(pr_no=pk)
    po = PurchaseOrder.objects.all()
    original_po_line = defaultdict(int)

    # Collect po_no values based on pr_no and line_no from PurchaseOrder
    for item in po:
        newValPo = json.loads(item.item_pr)
        for newItem in newValPo:
            pr_no = newItem['pr_no']
            line_no = newItem['line_no']
            original_po_line[(pr_no, line_no)] = item.po_no

    # Create a copy of original_po_line dictionary
    original_pr_line = original_po_line.copy()

    # Process the item_json from the PurchaseRequestNew object
    newValPr = json.loads(pr.item_json)
    print(newValPr)
    po_avilable_list = []
    for itemPr in newValPr:
        line_no = itemPr['line_no']
        pr_no = pk
        po_no = original_pr_line[(pr_no, line_no)]
        print(f"pr_no: {pr_no}, line_no: {line_no}, po_no: {po_no}")
        
        remaining_dict = {
                    "line_no": line_no,
                    "material_name" : itemPr["material_name"],
                    "material_unit":itemPr["material_unit"],
                    "po_no":po_no,   
                    "material_no":itemPr['material_no'],
                    "material_price" :itemPr['material_price'],
                    "material_text" :itemPr['material_text'],
                    "total_price":itemPr["total_price"],
                    "material_qty": itemPr["material_qty"],
                }
        po_avilable_list.append(remaining_dict)



    return json.dumps(po_avilable_list)


# orignal Prview  PrView 
class OrPurchaseRequestNewView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        if pk is not None:
            pr = PurchaseRequestNew.objects.get(pr_no=pk)
            pr_item = {"user" : pr.user,"time":pr.time,"item_json":prignalprpreview(pk)}
            serializer = PurchaseRequestSerializer(pr_item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            pr = PurchaseRequestNew.objects.all()
            serializer = PurchaseRequestSerializer(pr, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

  


# orignal PO view with no change if GRN created 
def poorignalpreview(pk):
    grn = GRN.objects.all()
    po = PurchaseOrder.objects.get(pk=pk)
    
    original_grn_line = defaultdict(int)
    for item in grn:
        newValPo = json.loads(item.item_po)
        for newItem in newValPo:
            po_no = newItem['po_no']
            po_line = newItem['po_line']
            original_grn_line[(po_no, po_line)] = item.grn_no
    

    original_po_line = original_grn_line.copy()

    newValPr = json.loads(po.item_pr)
    grn_avilable_list = []
    for itemPo in newValPr:
        po_line = itemPo['po_line']
        po_no = pk
        grn_no = original_po_line[(po_no, po_line)]
        print(f"po_no: {po_no}, po_linr: {po_line}, grn_no: {grn_no}")

        original_quantities_json = itemPr(itemPo["pr_no"])
        original_quantities = json.loads(original_quantities_json)

        original_qty_pr = 0
        for original_item in original_quantities:
            if original_item["line_no"] == itemPo["line_no"]:
                original_qty_pr = original_item["material_qty"]
                break
        
        remaining_dict = {
                    "line_no":itemPo["line_no"],
                    "pr_no" :itemPo["pr_no"],
                    "po_no":po_no,   
                    "po_line": po_line,
                    "grn_no":grn_no,
                    "material_no":itemPo['material_no'],
                    "material_name" : itemPo["material_name"],
                    "material_unit":itemPo["material_unit"],
                    "material_price" :itemPo['material_price'],
                    "material_text" :itemPo['material_text'],
                    "material_tax": itemPo["material_tax"],
                    "total_amount":itemPo["total_amount"],
                    "total_tax":itemPo["total_tax"],
                    "material_qty": int(itemPo["material_qty"]),
                    "orignaQtyPr" : original_qty_pr
                                   
                }
        grn_avilable_list.append(remaining_dict)

    return json.dumps(grn_avilable_list) 



# orignal PO view 
class OrPuchaseOrderView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes =[IsAuthenticated]
    def get(self,request,pk=None,format=None):
        if pk is not None:
            po = PurchaseOrder.objects.get(po_no=pk)
            po_item = {"user" : po.user,"time":po.time,"item_pr":poorignalpreview(pk),"vendor_address":po.vendor_address,"delivery_address":po.delivery_address,"maindata":po.maindata,"po_no":pk}
            serilizer = PurchaseOrderSerilizer(po_item)
            return Response(serilizer.data,status=status.HTTP_200_OK)
        else:
             po = PurchaseOrder.objects.all()
             serilizer = PurchaseOrderSerilizer(po,many=True)
             return Response(serilizer.data,status=status.HTTP_200_OK) 