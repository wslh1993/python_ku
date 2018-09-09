from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm
from .models import *
from django.core.paginator import Paginator

def index(request):
    """首页"""
    categories = Category.objects.all()
    return render(request, 'index.html', {
        'categories': categories,
        'user': request.session.get('user')
    })

def register(request):
    # 注册
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        email = request.POST.get('email')
        # 正则验证数据
        # 使用模型类添加用户
        user = User.objects.create(username=username, password=password, email=email)  # 只写一个密码是因为数据库只有一个密码
        if user is not None:
            return redirect('login')
        else:
            return HttpResponse('注册失败')
    else:
        return render(request, 'register.html')

def login(request):
    """用户登录处理"""
    if request.method == 'POST':
        # 用表单提交过来的数据创建一个LoginForm对象
        form = LoginForm(request.POST)
        # 判断表单数据是否合法
        if form.is_valid():
            data = form.cleaned_data
            try:
                user = User.objects.get(
                    username=data['username'],
                    password=data['password']
                )
            except Exception:
                return HttpResponse('用户名密码错误')
            # 登录成功, 需要将当前登录的用户保存记录下来
            # 使用session存储数据，可以在服务端进行全局共享
            request.session['user'] = user.serializable_value('username')
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    # 清空session
    request.session.clear()

    return redirect('index')


def detail(request):
    #商品详情
    goods_id = request.GET.get('goods_id')
    good = Goods.objects.get(pk=goods_id)
    return render(request,'detail.html',{'goods':good,'user': request.session.get('user')})


def goods_list(request):
    #列表页面
    gjz = request.GET.get('q')

    if gjz != None:
        try:
            goods = Goods.objects.filter(name__contains=gjz)
        except Exception:
            return HttpResponse('不存在商品')
        # 3. 初始化Paginator分页类的对象
        paginator = Paginator(goods, 2)
        # 4. 获取页码
        num = request.GET.get('num', 1)
        # 5. 通过页码初始化当前页面的Page对象
        page = paginator.page(num)
        # 6. 返回响应结果
        return render(request, 'list.html', {
            'page': page,

            'q':gjz,
            'user': request.session.get('user')
        })
    # 1. 获取分类ID
    category_id = request.GET.get('category_id')

    # 2. 根据分类ID查询该分类下面的所有商品
    try:
        goods = Category.objects.get(pk=category_id).goods_set.all()
    except Exception:
        return HttpResponse('不存在商品')
    # 3. 初始化Paginator分页类的对象
    paginator = Paginator(goods, 2)
    # 4. 获取页码
    num = request.GET.get('num', 1)
    # 5. 通过页码初始化当前页面的Page对象
    page = paginator.page(num)
    # 6. 返回响应结果
    return render(request, 'list.html', {
        'page': page,
        'category_id': category_id,
        'user': request.session.get('user')
    })



def add_to_cart(request):
    # 获取请求提交的商品id和数量

    goods_id = request.POST.get('goods_id')
    number = request.POST.get('number')
    try:
        # get_or_create 返回 (object, created) object是数据对象，
        # created为布尔值，true为创建的数据，false为查询的数据
        # 获取当前用户的购物车
        cart = Cart.objects.get_or_create(
            user__username=request.session.get('user'),
            defaults={
                'user_id': User.objects.get(username=request.session.get('user')).id
            }
        )
    except Exception:
        return HttpResponse('没有该用户')
    # 给当前用户的购物车添加或更新商品数量
    cartgoods = CartGoods.objects.update_or_create(cart=cart[0], goods_id=goods_id)
    cartgoods[0].number += int(number)
    cartgoods[0].save()

    if cartgoods[0]:
        return HttpResponse(cart[0].cartgoods_set.count())
    else:
        return HttpResponse('添加失败')

def cart(request):
    #购物车
    cart = Cart.objects.get(user__username=request.session.get('user')).cartgoods_set.all()
    num = cart.count()
    return render(request, 'cart.html',{'cart':cart,'num':num,'user': request.session.get('user')})


def change(request):
    #购物车中修改数量随之更新数据库
    goods_id = request.POST.get('id')
    goods_num = request.POST.get('number')
    print(goods_num)
    CartGoods.objects.filter(id=goods_id).update(number=goods_num)
    return HttpResponse('1')


def order(request):
    # 获取到被选中到商品的ID们
    ids = request.GET.get('ids')
    n = ids.strip().split(',')
    cartgoods = CartGoods.objects.filter(id__in=n)
    print(cartgoods)
    return render(request, 'place_order.html', {'cartgoods': cartgoods,'user': request.session.get('user')})

def add(request):
    #添加商品订单 订单商品
    user_id = User.objects.get(username=request.session.get('user')).id
    print(user_id)
    ordergoods_id = request.POST.get('ordergoods_id')
    aa = ordergoods_id.strip().split(',')
    print(aa)
    cartgoods = CartGoods.objects.filter(id__in=aa)
    print(cartgoods)
    order = OrderInfo.objects.create(user_id=user_id,status=0,pay_status=0,shipping_status=0)
    for i in cartgoods:
         ordergoods = OrderGoods.objects.create(
             order_info=order,goods=i.goods,number=i.number
         )
    if ordergoods:
         CartGoods.objects.filter(id__in=aa).delete()
    return render(request,'user_center_order.html')

def center_info(request):
    #用户中心
    user_id = User.objects.get(username=request.session.get('user')).id
    xinxi = Userinfo.objects.get(user_id=user_id,id=1)
    return render(request,'user_center_info.html',{'user':request.session.get('user'),'xinxi':xinxi})

def center_order(request):
    #全部订单
    user_id = User.objects.get(username=request.session.get('user')).id
    dingdans = OrderInfo.objects.filter(user_id=user_id)
    print(dingdans)
    paginator = Paginator(dingdans, 2)
    # 4. 获取页码
    num = request.GET.get('num', 1)
    # 5. 通过页码初始化当前页面的Page对象
    page = paginator.page(num)
    # 6. 返回响应结果
    return render(request, 'user_center_order.html', {
        'page': page,
        'user': request.session.get('user')
    })


def center_site(request):
    #用户地址
    if request.method == 'POST':
        recipient = request.POST.get('recipient')
        address = request.POST.get('address')
        postcode = request.POST.get('postcode')
        phone = request.POST.get('phone')
        user_id = User.objects.get(username=request.session.get('user')).id
        user = Userinfo.objects.create(
            recipient=recipient,address=address,postcode=postcode,phone=phone,user_id=user_id
        )
        if user is not None:
            return render(request,'user_center_site.html',{'user':request.session.get('user')})
        else:
            return HttpResponse('提交失败')
    return render(request,'user_center_site.html',{'user':request.session.get('user')})
