# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .models import My_Data
from django.http import HttpResponse
import os, csv

import sys

# ------------------------------------------------------------------
def index(request):
    latest_list = My_Data.objects.order_by('no')[:10]
    context = {'latest_list': latest_list}
    return render(request, 'db_serv/index.html',context)
# ------------------------------------------------------------------
def detail(request):
 
    return render(request, 'db_serv/detail.html')
#
# ------------------------------------------------------------------
def file_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        sys.stderr.write("*** Enter POST file_upload *** aaa ***\n")
        if form.is_valid():
            sys.stderr.write("*** file_upload done *** aaa ***\n")
            rfile=handle_uploaded_file(request.FILES['file'])
            file_obj = request.FILES['file']
            sys.stderr.write(file_obj.name + "\n")
            
            print('file_path= ',rfile)
            f = open(rfile,'r',encoding='cp932')
            reader = csv.reader(f)
            ncnt=0
            for line in reader:
                ncnt=ncnt+1
                my = My_Data()
                print('***DB',my)
                print('data=',line[0],line[1],line[2])
                my.no = ncnt
                my.theme = line[1]
                my.bunrui1 = line[2]
                my.bunrui2 = line[3]
                my.bunrui3 = line[4]
                my.day_regist = line[5]
                my.day_modify = line[5]
                my.overview = line[6]
                my.description = line[7]
                my.keywords=''
                print('***count=',ncnt,'data=',my.theme,my.bunrui1,my.bunrui2)
                my.save()

            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'db_serv/upload.html', {'form': form})
#
#
# ------------------------------------------------------------------
def handle_uploaded_file(file_obj):
    sys.stderr.write("*** handle_uploaded_file *** aaa ***\n")
    sys.stderr.write(file_obj.name + "\n")
    file_path = 'media/documents/' + file_obj.name 
    sys.stderr.write(file_path + "\n")
    with open(file_path, 'wb+') as destination:
        for chunk in file_obj.chunks():
            sys.stderr.write("*** handle_uploaded_file *** ccc ***\n")
            destination.write(chunk)
            sys.stderr.write("*** handle_uploaded_file *** eee ***\n")
        return file_path
"""
    with open(file_path, 'w',encoding='utf-8') as destination:
        # read csv
        rdr = csv.reader(destination)
        # ignore header
        #next(rdr)
        # upsert
        ncnt=0
        for r in rdr:        
            ncnt=ncnt+1
            print('count= '+str(ncnt)+' theme= '+r[0]+' bunrui1= '+r[1])
"""
#
# ------------------------------------------------------------------
def success(request):
    str_out = "Success!<p />"
    str_out += "成功<p />"
    return HttpResponse(str_out)
# ------------------------------------------------------------------