from django.shortcuts import render,redirect
from .models import Medicine,UserProfile
from django.db.models import Q
from accounts.forms import RegistrationForm,add
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import get_object_or_404
# Create your views here.
def view_meds(request):
    medicine = Medicine.objects.all()
    x = ['1','2','3',]
    args={'medicine':medicine,'x':x}
    return render(request,'accounts/home.html',args)

def view_list(request):
    medicine = Medicine.objects.all()
    args={'medicine':medicine}
    return render(request,'accounts/list.html',args)

def search(request):
    query = request.GET.get("q")
    if query:
        items = Medicine.objects.filter(Q(name__icontains=query)|Q(price__icontains=query)|Q(company=query)).distinct()


    return render(request,'accounts/home.html',{'items':items})

@login_required
def profile(request):
    meds = Medicine.objects.filter(user=request.user)
    return render(request,'accounts/profile.html',{'meds':meds})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = RegistrationForm()


    return render(request,'accounts/register.html',{'form':form})

@login_required
def addmedicine(request):
    if request.method == 'POST':
        form1  = add(request.POST)
        if form1.is_valid():
            u1 = form1.save(commit=False)
            u1.user=request.user
            u1.created_date = timezone.now()
            u1.updated_date = timezone.now()
            u1.save()
            return redirect('/profile')
    else:
        form1  = add()
    return render(request,'accounts/addmed.html',{
        'form1':form1,
    })

@login_required
def update(request,pk=None):
    goo = get_object_or_404(Medicine,pk=pk)
    if request.method == 'POST':
        form = add(request.POST,instance=goo)
        if form.is_valid():
            good = form.save(commit=False)
            good.user = request.user
            good.updated_date = timezone.now()
            good.save()
            return redirect('/profile')
    else:
        form = add(instance=goo)


    return render(request,'accounts/upmed.html',{'form':form})

def delete_med(request,pk=None):
    if pk:
        Medicine.objects.get(pk=pk).delete()
    else:
        pass
    return redirect('/profile')
