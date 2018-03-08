from django.shortcuts import render
from django.views.generic import TemplateView

import json
from django.http import JsonResponse
def data(request):     
    x = ['2017-07-10', '2017-07-11', '2017-07-12', '2017-07-13', '2017-07-14']
    y = [58.13, 53.98, 67.00, 89.70, 99.00]
 
    mylist = []

    for intnum in range(5):
        mylist.append({"date" : x[intnum], "close" : y[intnum]})

    return JsonResponse(mylist, safe=False)
 
def d3sample(request):
    return render(request, 'd3sample.html', context=None)

