from django.shortcuts import render,HttpResponse,redirect
from . models import *

from django.contrib.auth.models import User
from django.contrib.auth import  authenticate,login,logout
from django.contrib import messages
from online_Courses.settings import *
import math
from time import time
from django.views.decorators.csrf import csrf_exempt

import razorpay
client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))

# Create your views here.

def index(request):
    courses = Courses.objects.all()
    param = {'courses':courses}
    return render (request, 'index.html',param)


def login_data(request):
    msg = ""
    if  request.method == "POST":
        name = request.POST.get('name',"")
        password = request.POST.get('pass',"")
        user = authenticate(username = name , password = password)
        if user :
            login(request,user)
            msg = "logging has been successfully "
        else:
            msg= "Invalid credentials ."
    return render (request, 'login.html',{'msg':msg})
    

        
def my_courses(request):
    if not  request.user.is_authenticated:
        return redirect('login')
    all_courses = UserCourse.objects.filter(user=request.user)

    return render(request,'my_courses.html',{'all_courses':all_courses})



def course_page(request,slug):
    course = Courses.objects.get(slug = slug)
    lecture_no = request.GET.get('lecture')
    videos=course.video_set.all().order_by('serial_number')
    if lecture_no == None:
        lecture_no = 1
    video = Video.objects.get(serial_number = lecture_no,course = course)
    if  (video.is_preview  is False):
        if (request.user.is_authenticated is False):
            return redirect('login')
        else:
            try:
                user_course = UserCourse.objects.get(user=request.user,course = course)
            except:
               return redirect('checkout',slug = course.slug)
        
    param = {'course':course, 'video':video,'videos':videos}
    return render (request, 'course_page.html',param)

def signup_page(request):
    msg = ""
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password =request.POST.get('password')
        if len(fname )<2:
            messages.success(request,"Name is too short ")
        try:
            myuser = User.objects.create_user(fname,email,password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request,"singup successfullly ")

        except User.DoesNotExist:
            messages.success(request,"authentication failed")
    return render (request, 'sign_up.html',{'msg': msg})

def Logout(request):
    logout(request)
    return redirect('/')

def checkout(request,slug):
    course = Courses.objects.get(slug=slug)
    user = None
    order = None
    payment = None
    if not  request.user.is_authenticated:
        return redirect('login')
    user = request.user
    action = request.GET.get('action')
    error = None
    if action == "create_payment":
        try:
            user_course = UserCourse.objects.get(user=user,course = course)
            error = "You are already enroll in this course "
           
        except:
           pass

        if error is  None:
            amount  = math.floor((course.price - (course.price * course.discount * 0.01))*100)
            currency = "INR"
            receipt = f"kirancode_{int(time())}"
            notes = {"email":user.email,"username":f"{user.first_name}{user.last_name}"}

            order = client.order.create({'amount' :amount, 'currency' : currency, 'receipt' : receipt,'notes' : notes})
            
            payment = Payment(order_id =order.get('id'),user = user,course= course)
            payment.save()

    param = {'course':course,'order':order,' payment':payment,'user':user,'error':error}

    return  render (request,'checkout.html',param)

@csrf_exempt
def varify_payment(request):
    if request.method == 'POST':   
        data = request.POST # {'razorpay_payment_id': ['pay_NrlCJQNRTw36ew'], 'razorpay_order_id': ['order_NrlBLzvdYRQ2lF'], 'razorpay_signature': ['44f734d0bb46af174a11763bb64dccb7ed42df39ea051fcb7888a1adbb7785e9']}> when payment is success then milta h
        context = {}
        try:
           client.utility.verify_payment_signature(data)
           razorpay_order_id = data['razorpay_order_id']
           razorpay_payment_id = data['razorpay_payment_id']
           payment = Payment.objects.get(order_id = razorpay_order_id)
           payment.payment_id =razorpay_payment_id
           payment.status = True
           usercourse =UserCourse(user = payment.user,course = payment.course )
           payment.user_course = usercourse
           usercourse.save()
           payment.save()

           return redirect('my_courses')
        except Exception as e:
            return HttpResponse(e)


def search(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        course_name = Courses.objects.filter(name__icontains = query)
        course_description = Courses.objects.filter(description__icontains = query)
        course_slug = Courses.objects.filter(slug__icontains = query)
        all_courses = course_name.union(course_description,course_slug)
        param = {'courses':all_courses}
    return render (request, 'index.html',param)