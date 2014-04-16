from django.shortcuts import render_to_response
from article.models import Article, File_Upload, Tram_File_Upload
from django.http import HttpResponse
from forms import ArticleForm
from forms import File_UploadForm, Tram_File_UploadForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.utils.encoding import smart_str
from django.core.files import File
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


# Create your views here.

def articles(request):
    return render_to_response('articles.html', {'articles': Article.objects.all()})
    #return HttpResponse(Article.objects.all())

def tram_file(request):
	return HttpResponse(Tram_File_Upload.objects.last().uploaded_file)
	#return render_to_response('tram_download.html', {'files': Tram_File_Upload.objects.last()})
	
	

@csrf_exempt
def tram_file_upload(request):
    msg = "Upload a file with new autonomous commands below."
    if request.POST:
        form = Tram_File_UploadForm(request.POST, request.FILES)
        form.save()
        msg = "Successfully uploaded a new command file. Click the back button to go back or upload another file with new autonomous commands below."
    

    form = Tram_File_UploadForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form
    args['msg'] = msg
    
    return render_to_response('tram_file.html', args)


def article(request, article_id=1):
    return render_to_response('article.html', {'article': Article.objects.get(id=article_id)})

def last_entry(request):
    return HttpResponse(Article.objects.last())

def last_entry_id(request):
    return HttpResponse(Article.objects.last().id)

def files(request):
    return render_to_response('files.html', {'files': File_Upload.objects.all()})

def file_(request, article_id=1):
    return render_to_response('file.html', {'file': File_Upload.objects.get(id=article_id)})

@login_required(login_url='/accounts/login/')
def file_upload(request):
    if request.POST:
        form = File_UploadForm(request.POST, request.FILES)
        form.save()

    form = File_UploadForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render_to_response('create_file.html', args)

@login_required(login_url='/accounts/login/')
def commands(request):
    if request.POST:
        form = ArticleForm(request.POST)
        form.save()
       # return HttpResponseRedirect('/articles/all')

#    else:

    form = ArticleForm()


    args = {}
    args.update(csrf(request))
    args['form'] = form
    
    last_command =""
    command = str(Article.objects.last()) 
    
    if(command == "measure 1 0 0 0 0"):
    	last_command = "Measure"
  
  	#elif(command == "measure 0 1 0 0 0"):
    	#last_command = "Take Pictures"
  
    #if(str(Article.objects.last()) == "measure 0 0 1 0 0"):
    #	last_command = "Take Video"
    
    #if(str(Article.objects.last()) == "measure 0 0 0 1 0"):
    #	last_command = "Livestream On"
  	
  #	if(str(Article.objects.last()) == "measure 0 0 0 0 1"):
   # 	last_command = "Livestream Off"
  		
  
  
    args['last_command'] = str(command)
    received_command = str(Article.objects.last()).lower()	    

    if("move" in received_command or "pciture" in received_command or "measure" in received_command or "wait" in received_command or "update_autonomous" in received_command or "disable_autonomous" in received_command or "enable_autonomous" in received_command):	
        args['is_valid'] = "The last command was valid."

    else:
		args['is_valid'] = "The last command was not valid please enter a valid command."

    args['user_name'] = str(request.user.username)		
    return render_to_response('commands.html', args)

	

    
	
