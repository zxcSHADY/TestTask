from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.contrib import messages

con = {'name': 'user', 'inf': 'Важная информация про что то'}
email = {'em': ""}

def main(request):
    return render(request, "main/registr.html")

def menu_reg(request):
    return render(request, "main/registr.html")

def login(request):
    return render(request, "main/log_in.html")

def edit_menu(request):
    return render(request, "main/edit_menu.html")

def EnterEm(request):
    if request.method == "POST":
        user_email = request.POST.get('logEM')
        email['em'] = user_email
        user_psw = request.POST.get('psw')
        if User.objects.get(email=user_email).groups.filter(name='admin').exists():
            con['name'] = 'admin'
            con['inf'] = 'Важная информация про что то для админа'
        if User.objects.get(email=user_email).groups.filter(name='guest').exists():
            con['name'] = 'guest'
            con['inf'] = 'Важная информация про что то для гостя'
        if User.objects.get(email=user_email).groups.filter(name='user').exists():
            con['name'] = 'user'
            con['inf'] = 'Важная информация про что то для User'
        if User.objects.filter(email=user_email).count() == 1:
            if User.check_password(User.objects.get(email=user_email), user_psw):
                return render(request, "main/site.html", con)
            else:
                return HttpResponse('password is wrong')
        else :
            return HttpResponse('No account')
        
def registrs(request):
    if request.method == "POST":
        reg_name = request.POST.get('regName')
        reg_em = request.POST.get('regEM')
        reg_psw = request.POST.get('regpsw')
        reg_pswR = request.POST.get('regpswR')
        if reg_psw == reg_pswR:
            if User.objects.filter(email=reg_em).count() == 0:
                User.objects.create_user(username=reg_name, email=reg_em, password=reg_psw)
                return render(request, "main/log_in.html")
            else:
                return HttpResponse('you already have an account')
        else:
            return render(request, "main/registr.html")
        
def edAp(request):
    if request.method == "POST":
        ed_name = request.POST.get('regName')
        del_acc = request.POST.get('del_acc')
        if del_acc:
            User.objects.get(email=email['em']).is_active = False
            User.objects.get(email=email['em']).save()
            User.objects.filter(email=email['em']).update()
        User.objects.filter(email=email['em']).update(username=ed_name)
        User.objects.get(email=email['em']).save_base()
        return HttpResponse(User.objects.get(email=email['em']).is_active)