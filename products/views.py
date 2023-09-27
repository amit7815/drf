from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer 

# Genreic API View

# class ProductCreateAPIView(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def perform_create(self, serializer):
#         print(serializer.validated_data)
#         title = serializer.validated_data.get("title")
#         # serializer.save()  when content is not present
#         content = serializer.validated_data.get("content") or None
#         if content is None:
#             content = title
#         serializer.save(content=content)    
#         # send a django signal

# product_create_view = ProductCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    # Product.objects.get(pk=15) here pk is look_up field


product_detail_view = ProductDetailAPIView.as_view()   # we can do like this as well but .as_view() is used by everyone

# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # lookup_field = 'pk'
#     # Product.objects.get(pk=15) here pk is look_up field


# product_list_view = ProductListAPIView.as_view()   # we can do like this as well but .as_view() is used by everyone

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    # Product.objects.get(pk=15) here pk is look_up field


product_list_create_view = ProductListCreateAPIView.as_view()   # we can do like this as well but .as_view() is used by everyone