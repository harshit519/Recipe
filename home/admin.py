from django.contrib import admin
from home.models import *
class harAdmin(admin.ModelAdmin):
  list_display = ("name", "study", "phone_no",'address','age')
admin.site.register(harshit,harAdmin)
admin.site.register(student)
admin.site.register(Department)
admin.site.register(StudentID)




# Register your models here.
