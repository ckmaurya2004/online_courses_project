from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Courses(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(null = True)
    discount = models.IntegerField(null = True,default = 0)
    slug =  models.CharField(max_length=100,null= False,unique=True)
    active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='images/thumbnail')
    resource = models.FileField(upload_to='images/resource')
    length =  models.IntegerField(null = True)

    def __str__(self):
        return self.name

class CourseDetails(models.Model):
    description = models.CharField(max_length=200)
    course = models.ForeignKey(Courses, on_delete = models.CASCADE)
    class Meta:
        abstract = True

    

class Tags(CourseDetails):
    def __str__(self):
        return self.description

class Prerequisite(CourseDetails):
    def __str__(self):
        return self.description


class Learning(CourseDetails):
   def __str__(self):
        return self.description
   
class Video(models.Model):
    title = models.CharField(max_length=100,null =False)
    course = models.ForeignKey(Courses, on_delete = models.CASCADE)
    serial_number = models.IntegerField()
    video_id = models.CharField(max_length=200,null =False)
    is_preview = models.BooleanField(default=False)


    def __str__(self):
        return self.title
    
class UserCourse(models.Model):
    user = models.ForeignKey(User,null = False,on_delete = models.CASCADE)
    course = models.ForeignKey(Courses,null = False, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.name}"
    

class Payment(models.Model):
    payment_id = models.CharField(max_length = 50)
    order_id = models.CharField(max_length =50,null = False)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    status = models.BooleanField(default = False)
    user_course = models.ForeignKey(UserCourse,null = True,blank = True,on_delete = models.CASCADE)
    course = models.ForeignKey(Courses,on_delete = models.CASCADE)
    data = models.DateTimeField(auto_now_add = True)

    def __str__(self):
            return f" {self.user_course}- {self.user.username}"
        
