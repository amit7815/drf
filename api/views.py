from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
# def api_home(request, *args, **kwargs):
#     # request --> HttpRequest instance from django 
#     # request.body
#     body = request.body  # byte string of JSON data
#     data = {}
#     try: 
#         data = json.loads(body)  #takes string of Json data and converts into python dictionory
#     except: 
#         pass
#     print(body)
#     print(data)
#     print(data.keys())  # dict_keys(['query'])
#     print(request.GET)  # url query parameter <QueryDict: {'abc': ['123']}>
#     print(request.POST)
#     data['headers'] = dict(request.headers)  # request.META will give all the headers
#     print(request.headers)
#     data['params'] = dict(request.GET)
#     data['content_type'] = request.content_type
#     # return JsonResponse({"message" : "hi there this is your Django api response!!"})
#     return JsonResponse(data)



# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first() # create random query set and grab one of those value

#     data = {}
#     if model_data:
#         data['id'] = model_data.id
#         data['title'] = model_data.title
#         data['content'] = model_data.content
#         data['price'] = model_data.price
#         # model instance (model_data)
#         # want to turn it into python dictionary
#         # serialization or return Json to my client
#     return JsonResponse(data)


# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first() # create random query set and grab one of those value

#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id', 'title']) # fields is optional if we want to include specific fields otherwise all fields
#     #     json_data_string = json.dumps(data)
#     return JsonResponse(data) # accepts dictionary as an argument
#     # return HttpResponse(json_data_string, headers={"content-type":"application/json"}) # accepts string, by default content-type is html/text

@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    """ 
    django rest framework views and response
    """
    model_data = Product.objects.all().order_by("?").first() # create random query set and grab one of those value

    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title']) # fields is optional if we want to include specific fields otherwise all fields
    #     json_data_string = json.dumps(data)
    return Response(data) # accepts dictionary as an argument
    # return HttpResponse(json_data_string, headers={"content-type":"application/json"}) # accepts string, by default content-type is html/text