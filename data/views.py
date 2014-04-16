from django.shortcuts import render, render_to_response
from data.models import Data, JSONModel, JSONModel_Tram
from forms import DataForm
from forms import JSONModelForm
from forms import JSONModel_Tram_Form

from article.models import Article
from article.forms import ArticleForm

from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.utils.encoding import smart_str
from django.core.files import File
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


import random
import datetime
import time
import json

# Create your views here.
@login_required(login_url='/accounts/login/')
def json_upload(request):
    if request.POST:
        form = JSONModelForm(request.POST)
        form.save()

    form = JSONModelForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render_to_response('upload_json.html', args)

# Create your views here.
@login_required(login_url='/accounts/login/')
def tram_data_upload(request):
    if request.POST:
        form = JSONModel_Tram_Form(request.POST)
        form.save()

    form = JSONModel_Tram_Form()

    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render_to_response('upload_tram_json.html', args)	
	


def table(request):
    json_data = JSONModel.objects.last().json_model
    names = []

    #add the names of the data set to the names array
    for it in range(1, len(json_data)+1):
        names.append(json_data["id_"+str(it)]['name'])


    #get the data values for each row
    data = []
    for cur_row in range(0, len(json_data["id_1"]["data"])):

        row = []
    
        for cur_data in range(1, len(json_data)+1):

            if(cur_data == 1):
                timestamp = int(json_data["id_"+str(cur_data)]['data'][cur_row])
                value = datetime.datetime.fromtimestamp(timestamp / 1000)
                row.append(value.strftime('%Y-%m-%d %H:%M:%S'))

            else:
		row.append(json_data["id_"+str(cur_data)]['data'][cur_row])


	data.append(row)
    data['id'] = cur_id
    return render_to_response('table.html', {'names': names, 'data':data})


def graph_multi(request, start, end):
    json_data = JSONModel.objects.last().json_model

    cur_id = JSONModel.objects.last().id
	
    xdata = map(int, json_data['id_1']['data'])
   
    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie = {"tooltip": {"y_start": "The value is ", "y_end": " "},
                   "date_format": tooltip_date}
	
    chartdata = {
        'x': xdata,
    }
	
	
    for i in range(int(start), int(end) + 1):
	chartdata["name"+str(i)] = json_data["id_"+str(i)]["name"]
	chartdata["y"+str(i)] = map(float, json_data["id_"+str(i)]['data'])
	chartdata["extra"+str(i)] = extra_serie
		
	
	
	
	
    charttype = "lineWithFocusChart"
    chartcontainer = 'linewithfocuschart_container'  # container name
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': True,
            'tag_script_js': False,
            'jquery_on_ready': False,
        }
    }
    data['id'] = cur_id
    return render_to_response('linewithfocuschart.html', data)
	
	
	
	
def graph(request, data_id):
    """
    graph the data page
    """

    json_data = JSONModel.objects.last().json_model

    id = "id_" + str(data_id)

    xdata = map(int, json_data['id_1']['data'])
    ydata = map(float, json_data[id]['data'])

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie = {"tooltip": {"y_start": "The value is ", "y_end": " "},
                   "date_format": tooltip_date}

    chartdata = {
        'x': xdata,
        'name1': json_data[id]['name'], 'y1': ydata, 'extra1': extra_serie,
    }

    charttype = "lineWithFocusChart"
    chartcontainer = 'linewithfocuschart_container'  # container name
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': True,
            'tag_script_js': False,
            'jquery_on_ready': False,
        }
    }
    return render_to_response('linewithfocuschart.html', data)


def get_latest_graph_id(request):
	return HttpResponse(JSONModel.objects.last().id)
	
def get_latest_traminfo_id(request):
	return HttpResponse(JSONModel_Tram.objects.last().id)
	
	
def get_latest_tram_data(request):
    json_data = JSONModel_Tram.objects.last().tram_info
	
    form = {}
	
	
    command = str(Article.objects.last()) 
    form['last_command'] = str(command)
    received_command = str(Article.objects.last()).lower()	    

    if("move" in received_command or "measure" in received_command or "wait" in received_command or "update_autonomous" in received_command or "disable_autonomous" in received_command or "enable_autonomous" in received_command or "accl_tol" in received_command or "msr_tol" in received_command or "accl_sen" in received_command):	
        form['is_valid'] = "The last command was valid."

    else:
	form['is_valid'] = "The last command was not valid please enter a valid command."
	
	
    
    form['name'] = "\n      SDP14: Team REST"
    form['position'] = json_data['position']
    form['position_percentage'] = json_data['pos_percentage']
    form['battery_info'] = json_data['battery_info']
    form['timestamp'] = json_data['timestamp']
    form['current_move'] = json_data['command_info']['current_command']
    form['current_move_status'] = json_data['command_info']['status']
    form['shutdown_info'] = json_data['shutdown_info']
  
    cur_id = JSONModel_Tram.objects.last().id
    form['id'] = int(cur_id)
	
    form['accelerometer'] = int(json_data['accelerometer'])
    command = str(Article.objects.last()) 
    form['command_is'] = command
	
	
    return HttpResponse(json.dumps(form))

	
@login_required(login_url='/accounts/login/')
def tram_info(request):
	
    if request.POST:
        form = ArticleForm(request.POST)
        form.save()
    
    cur_id = JSONModel_Tram.objects.last().id
	
    json_data = JSONModel_Tram.objects.last().tram_info
	
    form = {}
    form.update(csrf(request))
    form['user_name'] = str(request.user.username)
    form['form'] = ArticleForm()
	
    command = str(Article.objects.last()) 
    form['last_command'] = str(command)
    received_command = str(Article.objects.last()).lower()	    

    if("move" in received_command or "measure" in received_command or "wait" in received_command or "update_autonomous" in received_command or "disable_autonomous" in received_command or "enable_autonomous" in received_command or "accl_tol" in received_command or "msr_tol" in received_command or "accl_sen" in received_command):	
        form['is_valid'] = "The last command was valid."

    else:
	form['is_valid'] = "The last command was not valid please enter a valid command."
	
	
	
    form['name'] = "\n      SDP14: Team REST"
    form['position'] = json_data['position']
    form['position_percentage'] = json_data['pos_percentage']
    form['battery_info'] = json_data['battery_info']
    form['timestamp'] = json_data['timestamp']
    form['current_move'] = json_data['command_info']['current_command']
    form['current_move_status'] = json_data['command_info']['status']
    form['shutdown_info'] = json_data['shutdown_info']
    form['id'] = int(cur_id)
	
	
  #  accel_data = 0;
	
#    if(int(json_data['accelerometer']) != 0 or int(json_data['accelerometer']) !=1 or int(json_data['accelerometer']) != 2):
#    	accel_data = 0;
#    else:
#	accel_data = json_data['accelerometer']
	
    form['accelerometer'] = int(json_data['accelerometer'])
    command = str(Article.objects.last()) 
    form['command_is'] = command
	
    return render_to_response('tram_info.html', form)
	
