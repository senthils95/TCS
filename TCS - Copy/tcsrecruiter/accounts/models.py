from django.db import models


class Requirement(models.Model):
    rgs_id = models.CharField(max_length=200,primary_key=True)
    status = models.CharField(max_length=200,default='NULL')
    role = models.CharField(max_length=200)
    rskill = models.TextField()
    texp = models.DecimalField(max_digits=4, decimal_places=2)
    branch = models.CharField(max_length=200)
    iou = models.CharField(max_length=200)
    riou = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    asn_date = models.DateTimeField('date assigned')
    rbranch = models.CharField(max_length=200)
    sbranch = models.CharField(max_length=200)

class SourcingMasterTracker(models.Model):
    sl_no = models.IntegerField()
    dot = models.DateTimeField()
    branch = models.CharField(max_length=200)
    sname = models.CharField(max_length=200)
    snum = models.CharField(max_length=200)
    can_name = models.CharField(max_length=200)
    sdetail = models.CharField(max_length=200)
    main_skills = models.TextField()
    uname = models.CharField(max_length=200)
    cus_name = models.CharField(max_length=200)
    ep_num = models.CharField(max_length=200,primary_key=True)
    '''day = models.CharField(max_length=200)
    doi = models.DateTimeField()
    status = models.CharField(max_length=200)
    cont_num = models.IntegerField()
    email_id = models.EmailField(max_length=200)
    texp = models.DecimalField(max_digits=4,decimal_places=2)
    rexp = models.DecimalField(max_digits=4,decimal_places=2)
    cu_org = models.CharField(max_length=200)
    cu_loc = models.CharField(max_length=200)
    pref_loc = models.CharField(max_length=200)
    cu_ctc = models.DecimalField(max_digits=4,decimal_places=2)
    exp_ctc = models.DecimalField(max_digits=4,decimal_places=2)
    notice_period = models.IntegerField()'''