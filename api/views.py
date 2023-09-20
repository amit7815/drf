from django.shortcuts import render
from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):
    # request --> HttpRequest instance from django 
    # request.body
    body = request.body  # byte string of JSON data
    data = {}
    try: 
        data = json.loads(body)  #takes string of Json data and converts into python dictionory
    except: 
        pass
    print(body)
    print(data)
    print(data.keys())  # dict_keys(['query'])
    print(request.GET)  # url query parameter <QueryDict: {'abc': ['123']}>
    print(request.POST)
    data['headers'] = dict(request.headers)  # request.META will give all the headers
    print(request.headers)
    data['params'] = dict(request.GET)
    data['content_type'] = request.content_type
    # return JsonResponse({"message" : "hi there this is your Django api response!!"})
    return JsonResponse(data)