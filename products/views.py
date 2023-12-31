from rest_framework import authentication ,generics, mixins, permissions
from .models import Product
from .serializers import ProductSerializer 
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django .http import Http404
from django.shortcuts import get_object_or_404

# Genreic API View

# class ProductCreateAPIView(generics.CreateAPIView):
#     queryset = Prodeleteduct.objects.all()
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
    authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # lookup_field = 'pk'
    # Product.objects.get(pk=15) here pk is look_up field


product_list_create_view = ProductListCreateAPIView.as_view()   # we can do like this as well but .as_view() is used by everyone

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    # Product.objects.get(pk=15) here pk is look_up field

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


product_update_view = ProductUpdateAPIView.as_view()   # we can do like this as well but .as_view() is used by everyone

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    # Product.objects.get(pk=15) here pk is look_up field
    
    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)


product_delete_view = ProductDestroyAPIView.as_view()

class CreateApiView(mixins.CreateModelMixin, generics.GenericAPIView): #  this is our single create mixin view
    pass

class ProductMixinView(mixins.ListModelMixin, mixins.CreateModelMixin ,mixins.RetrieveModelMixin ,generics.GenericAPIView): # with the help of ListModelMixin we can use list method here and in generic ListAPIView or any view this is implemented by default
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs): # HTTP --> GET
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get("title")
        # serializer.save()  when content is not present
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content=content)
        

product_mixin_view = ProductMixinView.as_view()


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

