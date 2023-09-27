from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer 
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django .http import Http404
from django.shortcuts import get_object_or_404

# Genreic API View

# class ProductCreateAPIView(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def perform_create(self, serializer):
#         print(serializer.validated_data)
        # title = serializer.validated_data.get("title")
        # # serializer.save()  when content is not present
        # content = serializer.validated_data.get("content") or None
        # if content is None:
        #     content = title
        # serializer.save(content=content)    
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

@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method  # PUT --> uupdate, DESTROY --> delete

    if method == 'GET':
        if pk is not None:
            # queryset = Product.objects.filter(pk=pk)
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
            # if not queryset.exist():
            #     raise Http404
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
        # url_args
        # get request  --> detail view
        # list view

    if method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):  # for knowing the detailed error
            title = serializer.validated_data.get("title")
            # serializer.save()  when content is not present
            content = serializer.validated_data.get("content") or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=404) 
        # create an item

