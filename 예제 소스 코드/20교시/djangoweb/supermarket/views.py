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
    x = ['2017-07-10', '2017-07-11', '2017-07-12', '2017-07-13', '2017-07-14']
    y = [58.13, 53.98, 67.00, 89.70, 99.00]

    myData = json.dumps([{"date": x[i], "close": y[i]} for i in range(5)])
    return JsonResponse(myData, safe=False)


def d3sample(request):
    return render(request, 'd3sample.html', context=None)