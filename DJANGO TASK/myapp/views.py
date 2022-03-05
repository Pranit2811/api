from ast import Return
from asyncio import futures
from time import time
from django import urls
from .models import Item
from .serializers import ItemSchema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import concurrent.futures
import json
import requests
import threading
import time
from django.http import JsonResponse
# Create your views here.

@api_view(['GET'])
def getitem(request):
    itemlist = Item.objects.all()
    serialize = ItemSchema(itemlist,many=True)
    return Response(serialize.data)


@api_view(['POST'])
def additem(request):
    serialize = ItemSchema(data=request.data)
    if serialize.is_valid():
        serialize.save()
    else:
        return Response(serialize.errors,status.HTTP_400_BAD_REQUEST)
        
    return Response(serialize.data)





thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def read_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def read_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(read_site, sites)

def delaytimecounter(request,delay_value):
    # print(delay)
    sites = [f"https://httpbin.org/delay/{delay_value}",
       f"https://httpbin.org/delay/{delay_value}",
       f"https://httpbin.org/delay/{delay_value}",
       f"https://httpbin.org/delay/{delay_value}",
       f"https://httpbin.org/delay/{delay_value}",
       ] 
    start_time = time.time() 
    read_all_sites(sites)
    duration = time.time() - start_time
    print(f"time take {duration} seconds")
    return JsonResponse({"time_taken":duration})
      
