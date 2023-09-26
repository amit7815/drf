from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer 

# Genreic API View

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    # Product.objects.get(pk=15) here pk is look_up field


product_detail_view = ProductDetailAPIView.as_view()   # we can do like this as well but .as_view() is used by everyone