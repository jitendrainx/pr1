from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductSerializer,CategorySerializer
from .models import Product,Category
import openpyxl
from django.http import HttpResponse
from rest_framework.response import Response
import threading
import base64
import json
from .tasks import create_bulk_product
# Create your views here.


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset =  Product.objects.all()
    serializer_class = ProductSerializer

    # def list(self,request,*args,**kwargs):
    #     response=super().list(request,*args,**kwargs)
    #     data = json.dumps(response.data).encode()
    #     encrypted = base64.b64decode(data).decode()
    #     return Response({"data":encrypted})


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Product.objects.all()
    serializer_class = ProductSerializer


class ProductExportView(generics.ListAPIView):
    queryset =  Product.objects.all()
    serializer_class = ProductSerializer

    def list(self,request,*args,**kwargs):
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.title = "Products"

        worksheet.append(["Id","Category","Title","Descriptin","Price","Status","Created_at","Updated_at"])

        for product in self.get_queryset():
            worksheet.append([
                product.id,
                product.category.name,
                product.title,
                product.descriptin,
                product.price,
                product.status,
                str(product.created_at),
                str(product.updated_at)
            ])
        response = HttpResponse (
            content_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response['Content-Disposition'] = 'attachment; filename="products.xlsx"'
        workbook.save(response)
        return response

class BulkproductView(generics.GenericAPIView):
    queryset =  Product.objects.all()
    serializer_class = ProductSerializer

    def post(self,request,*args,**kwargs):
        try:
            count = int(request.data.get("count"))
        except Exception as e:
            return Response({"error":"count must be given"})
        
        res = create_bulk_product.delay(count)
        
        # def create_bulk_product(n):
        #     category = Category.objects.first()
        #     if not category:
        #         category = Category.objects.create(name="Default")
            
        #     product = []
            
        #     for _ in range(n):
        #         product.append(Product(
        #             category=category,
        #             title=f"auto-generate{_}",
        #             price = 100.00,
        #             status = True,
        #             descriptin = f"auto-description-{_}"
        #         ))
        #     Product.objects.bulk_create(product)

        # thread = threading.Thread(target=create_bulk_product,args=(count,))
        # thread.start()
        return Response(
            {"message":"process start"}
        )

            

