from faker import Faker
from .models import Department, StudentID, student
fake=Faker()
import random
def seed_db(n=20):
    try:
        departments_objs = list(Department.objects.all())
        if not departments_objs:
            departments_objs = [Department.objects.create(department='General')]
        for i in range (0,n):
            department = random.choice(departments_objs)
            student_id=F'STU-0{random.randint(100,1000)}'


            student_name=fake.name()
            student_age= random.randint(18,27)
            student_email= fake.email()
            student_address=fake.address()



            student_id_obj = StudentID.objects.create(student_id=student_id)


            student.objects.create(


                department=department,
                student_id=student_id_obj,
                student_name=student_name,
                student_age=student_age,
                student_email=student_email,
                student_address=student_address,

                        )
            
    except Exception as e:
        print(e)