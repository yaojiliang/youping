import random
import time
import datetime
import jwt
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from qiantai.models import UserInfo, Goods
from .tools.check_num import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

code=16834

# code=random.randint(10000,99999)
# globals(code)
def index(request):
    return render(request, 'qiantai/index.html')
def check_is_num(request):
    config = {
        "accountSid": "8aaf07086e0115bb016e45902a0b2710",  # 主账户id
        "appToken": "19a50abeaeb44b96a10654930d432c9c",  # 令牌
        "appId": "8aaf07086e0115bb016e45902a622716",  # 应用id
        "templateId": "1"  # 模版id
    }
    if request.method == 'GET':
        phone=request.GET.get('phone')
        print(phone)
        if not phone:
            return JsonResponse({'code':443})
        # TODO　这个可以判断一下数据库中是否存在这个号码,保证号码的唯一性
        yun=YunTongXin(**config)
        # TODO先注消掉
        # global code
        # code=random.randint(10000, 99999)
        phone_ischeck=phone
        res = yun.run(phone_ischeck, code)
        if res:
            result={'code':200,'data':[{'is_ok':True}]}
        else:
            result={'code':10001,'data':[{'is_ok':False}]}
        return JsonResponse(result)
    else:
        return JsonResponse({'code':10002,'data':{'error':'error'}})

def register(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        if not username:
            result = {'code':10003,'data':'请填写用户名！'}
            return JsonResponse(result)
        password1=request.POST.get('password')
        password2=request.POST.get('r_password')
        if password1 != password2:
            result={'code':10004,'data':'两次密码不一致'}
            return JsonResponse(result)
        user = UserInfo.objects.filter(username=username)
        if user:
            result={'code':10005,'data':'用户名已存在'}
            return JsonResponse(result)
        # 用md5生成密码
        pm = hashlib.md5()
        pm.update(password1.encode())

        phone=request.POST.get('phone')
        check_phone=request.POST.get('check_phone')
        email=request.POST.get('email')
        if not phone or not check_phone or not email:
            return JsonResponse({'code':10011,'data':'请正确填写'})
        # print(check_phone)
        # print(code)
        if code != int(check_phone):
            result = {'code':10006,'data':'验证码不正确'}
            return JsonResponse(result)
        try:
            UserInfo.objects.create(username=username,password=pm.hexdigest(),user_telphone=phone,userEmail=email)
            # print(pm)
        except Exception as e:
            print(e)
            return JsonResponse({'code':10007,'data':'用户名已经存在'})
        login_time = time.time()
        token =make_token(username,3600*24,login_time)
        result = {'code':200,
                  'data':{'token':token.decode()},
                  'username':username
                  }
        return JsonResponse(result)

def login(request):
    if request.method == 'POST':
        username=request.POST.get('login_username')
        if not username:
            return JsonResponse({'code':10003,'data':'请输入用户名'})
        try:
            user=UserInfo.objects.get(username=username)
        except Exception as e:
            print(e)
            return JsonResponse({'code':10009,'data':'没有此用户'})
        password = request.POST.get('login_password')
        pm=hashlib.md5()
        pm.update(password.encode())
        pwd = pm.hexdigest()
        if user.password != pwd:
            return JsonResponse({'code':10010,'data':'密码错误'})
        login_time=time.time()
        token = make_token(username, 3600 * 24, login_time)
        result = {
                    'code': 200,
                  'data': {'token': token.decode()},
                  'username': username
                  }
        return JsonResponse(result)

def logout(request):
    if request.method == 'GET':
        username=request.GET.get('username')
        # token = request.GET.get('token')
        if not username:
            return JsonResponse({'code':10013,'data':'没有此用户,退出有误！'})
        return JsonResponse({'code':200,'data':'ok'})

def detail(request):
    phone_id=request.GET.get('phone')
    try:
        phone=Goods.objects.get(goods_id=phone_id)
    except Exception as e:
        print(e)
        return JsonResponse({'code':'10020','data':'没有款手机'})
    dic={'phone':phone}
    return render(request,'qiantai/deail.html',dic)

def add_shoppingcar(request):
    if request.method == 'GET':
        phone_id=request.GET.get('phone')
        try:
            phone=Goods.objects.get(goods_id=phone_id)
        except Exception as e:
            print(e)
            return JsonResponse('没有此款手机')
        market=phone.market_price

        return JsonResponse({})

    return JsonResponse({})

def phone(request):
    goods=Goods.objects.filter(brand=1)
    paginator=Paginator(goods,6)# 创建page对象
    page = request.GET.get('page',1)# 默认第一页

    try:
        page_phone = paginator.page(page)# 传给html当前页
    except PageNotAnInteger:
        page_phone = paginator.page(1)
    except EmptyPage:
        page_phone = paginator.page(paginator.num_pages)
    dic={'page_phone':page_phone}
    return render(request,'qiantai/phone.html',dic)

def pad(request):
    return render(request,'qiantai/pad.html')

def computer(request):
    return render(request,'qiantai/computer.html')




def make_token(username,exp,l_datetime):
    key = 'salt123'
    now_t=time.time()
    playload = {'username':username,'exp':int(exp+now_t),'login_time':l_datetime}
    return jwt.encode(payload=playload,key=key,algorithm='HS256')
