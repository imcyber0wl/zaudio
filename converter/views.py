#when deploying on linux include every path in os.path.normcase(), this was originally written and tested on windows 
from django.shortcuts import render
from .forms import FileForm
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .tasks import *
import random 
import subprocess
from celery import Celery
from django.http import JsonResponse, HttpResponse,FileResponse
import json
import time
import os

# Create your views here.
@csrf_exempt
def home(request):
    x=os.path.join(settings.BASE_DIR, "files")
    #y=str(settings.BASE_DIR)+"files"
    #print(y,type(y))
    #print(x,type(x))
    values=['aac','wav','mp3','ogg','mp4','flv']
    form=FileForm()
    
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)

        if form.is_valid():
            file_list=['file','file2','file3','file4',
                       'file5','file6','file7','file8']
            file_list2=[]
            
            formats=['format1','format2','format3','format4','format5',
                     'format6','format7','format8']
            formats2=[]
            
            for format_ in formats:
                formats2.append(form.cleaned_data[format_])
            
            for file in file_list:
                try:
                    request.FILES[file]
                    ext=request.FILES[file].name
                    ext=ext[len(ext)-3:len(ext)]
                    if ext in values:
                        file_list2.append(file)
                    else:
                        pass #skip any unsupported file type
                except:
                    print(file,"was not uploaded")  ###added this 
                    file_list2.append("x")          ###added this
                    pass

            c=0
            js_list=''
            for file in file_list2:
                if file=="x": ###added this
                    js_list+=file+'/' ###added this
                else:###added this
                    path,input_file=handle_uploaded_file(request.FILES[file])
                    js_list+=(input_file[0:len(input_file)-3]+formats2[c])+'/' #new file
                    #print(input_file[0:len(input_file)-3]+formats2[c])
                    convert_audio.delay(path,input_file,formats2[c])
                    c+=1

            '''ff=''
            c=0
            for file in js_list:
                if c==0:
                    ff="file="+file+"&"
                else:
                    ff+="file"+str(c)+"="+file+"&"

                c+=1'''

            return render(request,'wait.html',{'files':js_list,'ff':js_list}) ###added this
            
                
    return render(request,'home.html',{'form':form,'values':values})


def handle_uploaded_file(f):
    rn_name=random.randint(100,20000)
    path=str(settings.BASE_DIR)+"\\files\\"
    with open(path+str(rn_name)+f.name, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return path,str(rn_name)+f.name


def download_view(request,file1,file2,file3,file4,file5,file6,file7,file8): ###added this
    files=[]
    file_list=[file1,file2,file3,file4,file5,file6,file7,file8] ###added this
    for file in file_list:
        try:
            if file=="x": ###added this
                pass###added this
            else:###added this
                files.append(file)
        except:
            pass

    print(files)
    return render(request,'download.html',{'files':files})
        

@csrf_exempt
def check_file(request):
    data=json.loads(request.body)
    file= data['file']
    path=str(settings.BASE_DIR)+"\\files\\"
    result=404
    try:
        open(path+file,"r")
        result=200
    except:
        pass
    return HttpResponse("Text only, please.", status=result)
    

def download(request):
    try:
        #filename=request.GET['file']
        return FileResponse(open(str(settings.BASE_DIR)+'\\files\\'+filename, 'rb'), as_attachment=True)
    except:
        return HttpResponse("Access denied",status=403)
        
