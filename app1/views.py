from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect,Http404
from django.shortcuts import reverse
from app1.models import RegisteredDetails
def home(request):
    return render(request,'home.html',context=None)
'''
def registration(request):
    form = RegistrationForm()
    if request.method=='POST':
        form =RegistrationForm(request.POST)
        if form.is_valid():
    return render(request,'registration.html',context={'form_1':form})
'''
def regForm(request):
    return render(request,'reg.html',context=None)

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        project_domain=request.POST['p_domain']
        project_name=request.POST['p_name']
        phone_no=request.POST['phone']
        try:
            obj =RegisteredDetails(name=name,email=email,poject_domain=project_domain,project_name=project_name,phone_no=phone_no)
            obj.save()

        except Exception as e:
            return(HttpResponse('<script> error</script>'))

    return HttpResponseRedirect(reverse('app1:index'))


def viewReg(request):
    try:
        reg=RegisteredDetails.objects.all()
    except Exception as e:
        return HttpResponse('<script>alert(oops something went wrong,,cannot fetch datas)</script>')
    return render(request,'view.html',context={'obj':reg})

def find_us(request):
    return render(request, 'map.html', context = None)


def projects(request):
    return render(request, 'projects.html', context = None)
