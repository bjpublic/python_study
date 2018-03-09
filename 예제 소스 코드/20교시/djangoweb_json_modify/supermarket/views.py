from django.shortcuts import render
from django.views.generic import TemplateView
 
# Create views
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

from .models import Supermarket
 
def supermk(request):
    supers = Supermarket.objects.all()
    return render(request, 'super.html', {'supers': supers})

import json
import numpy as np
from django.http import JsonResponse
def data(request):     
    x = np.array(['2017-07-10', '2017-07-11', '2017-07-12', '2017-07-13', '2017-07-14'])
    y = np.array([58.13, 53.98, 67.00, 89.70, 99.00])
 
    mylist = []

    for intnum in range(5):
        mylist.append({"date" : x[intnum], "close" : y[intnum]})

    return JsonResponse(mylist, safe=False)
 
def d3sample(request):
    return render(request, 'd3sample.html', context=None)