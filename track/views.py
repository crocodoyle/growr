from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from track.models import Kid, Measurement

import subprocess
import growr.settings as settings

import graph, os, sys

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from track.models import Kid, Measurement

def index(request):
    latest_kid_list = Kid.objects.order_by('-first_name')[:5]
    context = {'latest_kid_list': latest_kid_list}
    return render(request, 'track/index.html', context)

def display(request, kid_id):
    kid = get_object_or_404(Kid, id=kid_id)
    
    data = graph.importData("/tmp/wtageinf.xls")
    
    #print >>sys.stderr, np.shape(data['age'])
    #print >>sys.stderr, np.shape(data['b'][0,:])
    
    for p in np.arange(9):
        plt.plot(data['age'], data['b'][p][:])
                  
    print >>sys.stderr, '{0}/k{1}.png'.format(settings.MEDIA_ROOT, kid_id)
    plt.savefig('{0}/k{1}.png'.format(settings.MEDIA_ROOT, kid_id))
    
    return render(request, 'track/display.html', {'kid': kid})    

def measure(request, kid_id):

    k = get_object_or_404(Kid, id=kid_id)
    try:
        weight = request.POST['weight']
        height = request.POST['height']
        
    except (KeyError, k.DoesNotExist):
        return render(request, 'track/display.html', {
            'kid': k,
            'error_message': "Couldn't find the kid in the system.",
        })
    else:
        m = Measurement()
        m.weight = weight
        m.height = height
        
        k.weight = weight
        k.height = height
        
        k.save()
        m.save()

        return HttpResponseRedirect(reverse('display', args=(k.id,)))
    
    #return HttpResponse("Measure me.  Bitch.")

def update(request):
    os.chdir('/tmp/')
    subprocess.call(['wget', 'http://www.cdc.gov/growthcharts/data/zscore/wtageinf.xls'])  
    
    data = graph.importData("/tmp/wtageinf.xls")
    
    
    return HttpResponse('Yo, updated bitch')

