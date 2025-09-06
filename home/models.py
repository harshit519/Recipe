from django.db import models

# Create your models here.

class harshit(models.Model):
    name=models.CharField(max_length=50)
    study=models.CharField(max_length=100)
    phone_no=models.IntegerField()
    address=models.TextField()
    age=models.IntegerField(default=21)


    def __str__(self) -> str:
        return f'{self.name}'
       
class Department(models.Model):
    department=models.CharField(max_length=100 ,default='ece')



    def __str__(self) -> str:
        return f'{self.department}'
    
    class Meta:
        ordering=['department']

class StudentID(models.Model):
    student_id=models.CharField(max_length=100,null=True)

    def __str__(self) -> str:
        return f'{self. student_id}'
       
class student(models.Model):
    department=models.ForeignKey(Department,related_name='depart',on_delete=models.CASCADE, null=True)
    student_id=models.OneToOneField(StudentID,related_name='studentid',on_delete=models.SET_NULL, null=True ,blank=True) 
    student_name=models.CharField(max_length=100,null=True)
    student_age=models.IntegerField(default=18 ,null=True)
    student_email=models.EmailField(unique=True,null=True)
    student_address=models.TextField(null=True)

    def __str__(self) -> str:


        return f'{self. student_name}'
    


    class Meta:
         ordering=['student_name']
         verbose_name='student'