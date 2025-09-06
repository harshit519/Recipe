from django.shortcuts import render
from .models import student

bc=[

   [ "harshit",45,77,"tiwari"],["abc",66,55]
]
k=["bbb",77,00]



def home(request):
  
   
    return render(request,'index.html', context={'page':'home page','bc':bc,'k':k})

def about(request):
    queryset = student.objects.select_related('department', 'student_id').all()
    return render(request,'about.html',context={'page':'about','student': queryset})

def contact(request):
   
    return render(request,'contact.html', context={'page': 'submit'})


