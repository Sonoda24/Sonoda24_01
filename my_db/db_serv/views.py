# Create your views here.
from django.http import HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render
from .forms import UploadFileForm
from .models import My_Data
from .models import My_Svg
from django.http import HttpResponse
from django.http import Http404
from django.http import JsonResponse
import os, csv
import sys
import re
from six.moves.html_entities import codepoint2name, name2codepoint
from six import unichr

db_data=''
svg_data=''
# ------------------------------------------------------------------
def index(request):
    context = {}
    return render(request,'db_serv/index.html',context)
# ------------------------------------------------------------------
def list(request):
    latest_list = My_Data.objects.order_by('no')[:100]
    context = {'latest_list': latest_list}
    return render(request, 'db_serv/list.html',context)
# ------------------------------------------------------------------
def new_list(request):
    context = {}
    return render(request, 'db_serv/new_list.html',context)
# ------------------------------------------------------------------
def get_combo(request):
    tex = request.GET.get("message")
    print("**get_combo** recieve "+ tex);
    result = My_Data.objects.all().order_by('no')
    print('records = ',result.count())
    i=0
    for data in result:
        if(i==0):
            gMydbid=str(data.no)
            gComboA=data.theme
            gComboB=data.bunrui1
            gComboC=data.bunrui2
            gComboD=data.bunrui3
            gComboE=data.day_regist
            gComboF=data.overview
        else:
            #print(' record=',data.no,data.theme,data.overview)
            gMydbid=gMydbid+";,;"+str(data.no)
            gComboA=gComboA+";,;"+data.theme
            gComboB=gComboB+";,;"+data.bunrui1
            gComboC=gComboC+";,;"+data.bunrui2
            gComboD=gComboD+";,;"+data.bunrui3
            gComboE=gComboE+";,;"+data.day_regist
            gComboF=gComboF+";,;"+data.overview
        i=i+1

    context = {
	'no':gMydbid,
	'theme':gComboA,
	'bunrui1':gComboB,
	'bunrui2':gComboC,
	'bunrui3':gComboD,
	'day_regist':gComboE,
	'overview':gComboF,
        }
#    print('** theme data **',gComboA);
    return JsonResponse(context)
#    return HttpResponse(context)
#    return render(request, '',context)
#    return render(request, 'db_serv/get_combo.html',context)
# ------------------------------------------------------------------
def detail(request, data_id):
    global db_data,svg_data
    try:
        db_data = My_Data.objects.get(pk=data_id)
        view_tex=db_data.description
        print('Db_data',db_data.overview)
        svg_data=My_Svg.objects.get(pk=data_id)
        svg_field=''
        if(svg_data.svg_tags!=''):
            svg_field = svg_data.svg_tags
            svg_field=svg_field.strip()
            print('**Svg=',svg_field)
        context = {
            'view_tex': view_tex,
            'svg_field': svg_field,
            }
    except My_Data.DoesNotExist:
        raise Http404("da_data does not exist")
    return render(request, 'db_serv/detail.html', context)
#def detail(request,data_id):
# 
#    return render(request, 'db_serv/detail.html')
#]
def update(request):
    global db_data,svg_data
    tex = request.GET.get("description")
    svg_field = request.GET.get("svg")
    svg_field=svg_field.strip()
    print('***Update data=',tex)
    print('***SVG data=',svg_field)
    db_data.description = tex
    svg_data.svg_tags=svg_field
    db_data.save()
    svg_data.save()
    return HttpResponse('update!')    
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
                my.overview = decode(line[6])
                my.description = decode(line[7])
                my.keywords=''
                print('***count=',ncnt,'data=',my.theme,my.bunrui1,my.bunrui2)
                my.save()
                mysvg=My_Svg()
                mysvg.no=ncnt
                mysvg.svg_tags=''
                mysvg.save()
                
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
def encode(source):
    new_source = ''

    for char in source:
        if ord(char) in codepoint2name:
            char = '&%s;' % codepoint2name[ord(char)]
        new_source += char

    return new_source
# ------------------------------------------------------------------
def decode(source):
    for entitie in re.findall('&(?:[a-z][a-z0-9]+);', source):
        entitie = entitie.replace('&', '')
        entitie = entitie.replace(';', '')
        source = source.replace('&%s;' % entitie, unichr(name2codepoint[entitie]))
    return source
# ------------------------------------------------------------------
