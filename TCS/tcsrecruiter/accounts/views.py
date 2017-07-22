from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponse
from _compact import JsonResponse
from django import forms
import django_excel as excel
from accounts.models import Requirement,Tracker
from django.template.response import TemplateResponse
from django.db.models import Q

data = [
    [1, 2, 3],
    [4, 5, 6]
]

# Create your views here.
def home(request):
	return render(request,'accounts/home.html')

def upload_form(request):
	return render(request,'accounts/upload_form.html')

class UploadFileForm(forms.Form):
    file = forms.FileField()

def import_sheet(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)
        if form.is_valid():
            print "inform"
            request.FILES['file'].save_to_database(
                name_columns_by_row=0,
                model=Requirement,
                mapdict=['rgs_id', 'rgs_id_status', 'role', 'rskill', 'texp', 'branch', 'iou', 'riou', 'name', 'asn_date', 'rbranch', 'sbranch'])
            return render(request,"accounts/home.html")
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {'form': form})

def import_source(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)
        if form.is_valid():
            print "in form"
            request.FILES['file'].save_to_database(
                name_columns_by_row=0,
                model=Tracker,
                mapdict=['sl_no', 'dot', 'branch', 'sname', 'snum', 'can_name', 'sdetail', 'main_skills', 'uname', 'cus_name', 'ep_num', 'day', 'doi', 'status', 'cont_num', 'email_id', 'texp', 'rexp', 'cu_org', 'cu_loc', 'pref_loc', 'cu_ctc', 'exp_ctc', 'notice_period'])
            print "in form 2"
            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {'form': form})

#variables passed to approval.html
#viou-iou variable 
#vbranch-branch variable
#vaccount-account variable
def view_approval(request):
    approval_data = Requirement.objects.all()
    viou = Requirement.objects.order_by().values('iou').distinct()
    vbranch = Requirement.objects.order_by().values('branch').distinct()
    vaccount = Requirement.objects.order_by().values('name').distinct()  
    return TemplateResponse(request, 'accounts/view_approval.html', {"approval_data": approval_data,"viou":viou,"vbranch":vbranch,"vname":vaccount})
    
def view_source(request):
    source_data = Tracker.objects.all()
    
    return TemplateResponse(request, 'accounts/view_source.html', {"source_data": source_data})

def export_data(request):
        return excel.make_response_from_a_table(
            Requirement, 'xlsx', file_name="ApprovalMasterSheet")

def view_filtered(request):
    print request.POST.getlist('viou')#viou is the name given in the approval.html for checkbox for iou
    fiou = request.POST.getlist('viou')
    fbranch = request.POST.getlist('vbranch')
    fname = request.POST.getlist('vname')
    btype = request.POST.get('type')
    flag = True
    if btype == 'Filter':
        if fiou:
            flag = False
            print ("inif")
            approval_dataiou = Requirement.objects.filter(iou__in = fiou)
        else:
            approval_dataiou = Requirement.objects.all()
            
            '''viou = Requirement.objects.order_by().values('iou').distinct()
            vbranch = Requirement.objects.order_by().values('branch').distinct()
            vaccount = Requirement.objects.order_by().values('name').distinct()'''
        if fbranch:
            flag = False
            approval_databr = Requirement.objects.filter(branch__in = fbranch)

        else:
            approval_databr = Requirement.objects.all()
           
        if fname:
            flag = False
            approval_dataname = Requirement.objects.filter(name__in = fname)
        else:
            approval_dataname = Requirement.objects.all()

        approval_data = (approval_dataiou&approval_dataname&approval_databr).distinct()
        if flag:
            approval_data = Requirement.objects.all() 
        return TemplateResponse(request, 'accounts/filter.html', {"approval_data": approval_data})

    elif btype == 'Clear':
        return redirect('/account/view_approval/')



def edit_view(request):
    global eid
    btype = request.POST.get('type')
    eid = request.POST.get('ergs_id')
    if btype == 'EDIT':       
        approval_data = Requirement.objects.filter(rgs_id__in = eid)
        return TemplateResponse(request, 'accounts/edit view.html', {"approval_data": approval_data})

    elif btype == 'DEL':
        Requirement.objects.filter(rgs_id__in = eid).delete()
        return redirect('/account/view_approval/')

def update_db(request):
    urgs_id = request.POST.get('rgs_id')
    uold_rgs_id= request.POST.get('old_rgs_id')
    urgs_id_status = request.POST.get('rgs_id_status')
    urole= request.POST.get('role')
    urskill = request.POST.get('rskill')
    Requirement.objects.filter(rgs_id__in = eid).update(rskill = urskill,role = urole,rgs_id_status = urgs_id_status ,old_rgs_id = uold_rgs_id, rgs_id = urgs_id)
    return redirect('/account/view_approval/')



          
