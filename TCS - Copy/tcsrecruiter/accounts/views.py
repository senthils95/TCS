from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse
from _compact import JsonResponse
from django import forms
import django_excel as excel
from accounts.models import Requirement,SourcingMasterTracker

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

'''def import_sheet(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)
        if form.is_valid():
            request.FILES['file'].save_to_database(
                name_columns_by_row=0,
                model=Requirement,
                mapdict=['rgs_id', 'status', 'role', 'rskill', 'texp', 'branch', 'iou', 'riou', 'name', 'asn_date', 'rbranch', 'sbranch'])
            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {'form': form})'''

def import_source(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)
        if form.is_valid():
            request.FILES['file'].save_to_database(
                name_columns_by_row=0,
                model=SourcingMasterTracker,
                mapdict=['sl_no', 'dot', 'branch', 'sname', 'snum', 'can_name', 'sdetail', 'main_skills', 'uname', 'cus_name', 'ep_num'])
            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {'form': form})
