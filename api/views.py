from rest_framework.views import APIView
from .serializers import ProductSerialzier
from .models import Product
from rest_framework.response import Response

class ProductView(APIView):

    query_set = Product.objects.all()

    def get(self,request):
        return Response(ProductSerialzier(self.query_set,many=True).data)

    def post(self,request):
        body = ProductSerialzier(data=request.data)

        if body.is_valid():
            body.save()
            return Response({'message','Ok!'})
        return Response({'message':body.errors})