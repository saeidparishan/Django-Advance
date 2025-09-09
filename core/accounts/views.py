import time
import requests

from django.shortcuts import render
from django.http import HttpResponseGone, JsonResponse
from django.core.cache import cache
from django.views.decorators.cache import cache_page

from .tasks import sendEmail


def send_email(request):
    sendEmail().delay()
    return HttpResponseGone('<h1>Done Sending</h1>')

# bedon decorators cach kardan
# def test(request):
#     if cache.get('test_delay_api') is None:
#         response = requests.get("https://6b9f4182-6a0d-4cd7-871f-43a69ec7b5bc.mock.pstmn.io/test/delay/5")
#         cache.set('test_delay_api',response.json())
#     return JsonResponse(cache.get('test_delay_api'))

# ba decorators 
@cache_page(60)
def test(request):
    response = requests.get("https://6b9f4182-6a0d-4cd7-871f-43a69ec7b5bc.mock.pstmn.io/test/delay/5")
    return JsonResponse(response.json())