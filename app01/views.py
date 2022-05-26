from django.shortcuts import render,HttpResponseRedirect
from django.contrib import auth
from app01.myform import User as FUser
from app01.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    user = request.session.get('user',False)

    return render(request,'app01/index.html',{'user':user})
#显示页面
def registerView(request):
    user = request.session.get('user', False)
    print(user)
    if not user:
        return render(request, 'app01/login.html')
    else :
        return HttpResponseRedirect('/index/')

#注册
def register(request):
    check = False
    if request.method == 'POST':
        form = FUser(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            user = User(**form.cleaned_data)
            user.save()
            check = True
            return render(request, 'app01/immediate.html',{'check':check})

    return HttpResponseRedirect('/index/')


#登录
def login(request):

    user = request.POST['username']
    password = request.POST['password']
    result = User.objects.get(username=user,password=password)

    if not result:
        return HttpResponseRedirect('/registerView/')
    else :
       request.session['user'] = user
       return HttpResponseRedirect('/index/')

#注销
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')