from django.db import models

'''
After making changes make sure you go to theathenaproject/athena and run
python manage.py makemigrations
python manage.py migrate
'''

class Student(models.Model):
    name = models.CharField(max_length=80)
    skill_add = models.IntegerField()
    skill_sub = models.IntegerField()
    skill_mul = models.IntegerField()
    skill_div = models.IntegerField()
    def __str__(self):
        return self.name+": "+str(self.skill_add)+", "+str(self.skill_sub)+", "+str(self.skill_mul)+", "+str(self.skill_div)

class History(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    performed_add = models.IntegerField()
    performed_sub = models.IntegerField()
    performed_mul = models.IntegerField()
    performed_div = models.IntegerField()
    date = models.DateTimeField()

class Worksheet(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    categories = models.CharField(max_length=300)
    solutions = models.CharField(max_length=300)
    levels = models.CharField(max_length=300)