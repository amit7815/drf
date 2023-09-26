from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'get_discount',
            'my_discount'
        ]

    def get_my_discount(self, obj):
        # print(obj.id)
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        # obj.user -> user.username
        try:
            return obj.get_discount()
        except:
            return None


# we can create as many as we want serializer for a same model
# class SecondProductSerializer(serializers.ModelSerializer):
#     my_discount = serializers.SerializerMethodField(read_only = True)
#     class Meta:
#         model = Product
#         fields = [
#             'title',
#             'content',
#             'price',
#             'sale_price',
#             'get_discount',
#             'my_discount'
#         ]

#     def get_my_discount(self, obj):
#         print(obj.id)
#         # obj.user -> user.username
#         return obj.get_discount()