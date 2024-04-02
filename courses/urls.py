
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.index,name = 'home'),
   path('course/<str:slug>',views.course_page,name = 'course'),
   path('signup/',views.signup_page,name ='signup'),
   path('login/',views.login_data,name ='login'),
   path('logout/',views.Logout,name ='logout'),
   path('checkout/<str:slug>',views.checkout,name ='checkout'),
   path('varify_payment',views.varify_payment,name ='varify_payment'),
   path('my_courses/',views.my_courses,name ='my_courses'),
   path('search/',views.search,name ='search'),

]
