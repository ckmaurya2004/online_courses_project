from django.contrib import admin
from . models import *

# Register your models here.

class TagAdmin(admin.TabularInline):
    model = Tags

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite

class VideogAdmin(admin.TabularInline):
    model = Video

class LearningAdmin(admin.TabularInline):
    model = Learning
class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin,PrerequisiteAdmin,LearningAdmin,VideogAdmin] 


admin.site.register(Courses,CourseAdmin)
admin.site.register((Video,UserCourse,Payment))

