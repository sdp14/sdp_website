from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
import datetime
import json
from django.core.files import File
from django.shortcuts import render, render_to_response



def hello(request):
    name = "SDP 2014: Team Remote Environmental Sensing Tram"  
    t = get_template('index.html')
    html = t.render(Context({'name':name}))
    return HttpResponse(html)

def post_logout(request):
    data = {}
    data['blank'] = ""
    return render_to_response('logout.html', data)
