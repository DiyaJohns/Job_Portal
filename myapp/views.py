from django.shortcuts import render
from myapp.models import CompanyReg,UserReg,AddVnc
from django.db.models.functions import Coalesce
from django.db.models import Max,Value
from datetime import date
# Create your views here
def index(request):
    return render(request,"index.html")
def reg(request):
    if request.method=="POST":
        cname=request.POST.get('name')
        clocation=request.POST.get('location')
        ctype=request.POST.get('comptype')
        email=request.POST.get('email')
        phone=request.POST.get('phno')
        uname=request.POST.get('username')
        password=request.POST.get('password')
        cr=CompanyReg(cname=cname,clocation=clocation,ctype=ctype,email=email,phone=phone,uname=uname,password=password)
        cr.save()
    return render(request,"index_reg.html")

def userreg(request):
    if request.method=="POST":
        fstname=request.POST.get('first-name')
        lstname=request.POST.get('last-name')
        addres=request.POST.get('address')
        quali=request.POST.get('qua')
        emailid=request.POST.get('your-email')
        phno=request.POST.get('phno')
        usrname=request.POST.get('uname')
        psword=request.POST.get('password')
        ur=UserReg(fname=fstname,lname=lstname,addrs=addres,qual=quali,email=emailid,phno=phno,uname=usrname,pswrd=psword)
        ur.save()
        ureg=UserReg.objects.all()
        return render(request,"index.html",{"ureg":ureg})
    return render(request,"index_ureg.html")
def login(request):
    if request.method=="POST":
        u=request.POST.get("username")
        p=request.POST.get("pass")
        found=0
        mrec=UserReg.objects.filter(uname=u,pswrd=p)
        if mrec.filter(uname=u,pswrd=p).exists():
            found=1
            for j in mrec:
                name=j.fname
                id=j.id
            request.session['id']=id
            request.session['fname']=name
            request.session['uname']=u
            request.session['pword'] = p
            request.session['rights'] ='user'
            return render(request,"userpage.html")
        if found==0:
            crec = CompanyReg.objects.filter(uname=u, password=p)
            if crec.filter(uname=u, password=p).exists():
                found = 1
                for j in crec:
                    name = j.cname
                    id = j.id
                request.session['id'] = id
                request.session['fname'] = name
                request.session['uname'] = u
                request.session['pword'] = p
                request.session['rights'] = 'company'
                return render(request, "companypage.html")

        if found==0:
            return render(request, "invalid.html")
    return render(request,"index_login.html")

def addvacancy(request):
    cid=request.session['id']
    name=request.session['fname']
    max_vno=AddVnc.objects.aggregate(max_vno=Coalesce(Max('vno'),Value(0)))['max_vno']
    vno=int(max_vno)+1
    if request.method=="POST":
        vname=request.POST.get('vname')
        pstno=request.POST.get('nop')
        sal=request.POST.get('slry')
        qual=request.POST.get('qual')
        va=AddVnc(vno=vno,vname=vname,salary=sal,nop=pstno,qual=qual,compid=cid,company=name)
        va.save()
    return render(request, "AddVacancy.html",{"vno":vno,"cid":cid,"name":name})


def viewvacancy(request):
    arec= AddVnc.objects.all()
    return render(request, "viewvacancy.html", {"arec":arec})
 #   appno=request.POST.get(a)
 #   apdt=request.POST.get()
 #   apid=request.POST.get()
  #  apnam=request.POST.get()
 #   vno=request.POST.get()
 #   job=request.POST.get()
 #   cid=request.POST.get()
 #   cnam=request.POST.get()
 #   st=request.POST.get()