from django.shortcuts import render, redirect
from .models import article
from .forms import UploadFileForm
import os, csv
from tkinter import messagebox

UPLOAD_DIR = os.path.dirname(os.path.abspath(__file__)) + '/data/'

def index(request):
    print('***Request= ',request,' method= ',request.method,' path= ',request.path,' contype= ',request.content_type)
    if request.method == 'POST':
        # POST
        form = UploadFileForm(request.POST, request.FILES)
        print('File Step1')
        if form.is_valid():
            # file is saved. by binary

            f = request.FILES['file']
            path = os.path.join(UPLOAD_DIR, f.name)
            print('File Step2 path= ',path)         
            """
            with open(path, 'wb') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
            """
            # open csv
            print('File Step3')
            with open(path, 'r',encoding='utf-8') as destination:
                # read csv
                rdr = csv.reader(destination)
                # ignore header
                next(rdr)
                # upsert
                print('File Step4')
                ncnt=0
                for r in rdr:
                    art = article()
                    art.theme = r[0]
                    art.bunrui1 = r[1]
                    art.bunrui2 = r[2]
                    art.bunrui3 = r[3]
                    art.overview = r[4]                    
                    art.save()
                    ncnt=ncnt+1
                    print('count= '+str(ncnt)+' theme= '+r[0]+' bunrui1= '+r[1])
                    if ncnt>50:
                        break
            return redirect('app:index')
            #return render(request, 'app/index.html', {'form':form})
    else:
        # GET
        print(' Upload Form generated ')
        messagebox.showinfo('確認', 'Ｕｎｌｏａｄフォームを表示します。')
        form = UploadFileForm()
        #qry = article.objects.order_by('-ym')[:1].values('ym','homogeneity','plowing','biological','chemical','hardness')
        return render(request, 'app/index.html', {'form':form})