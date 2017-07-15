import django
import os, shutil, random, sys
from django.utils import timezone

# tell django where the settings are
os.environ['DJANGO_SETTINGS_MODULE'] = 'theathenaproject.settings'
django.setup()

from athena.models import Student, Worksheet
from athena import create_problems

print('Clear Students Table:')
Student.objects.all().delete()

print('Make Students:')
Student.objects.create(name="Shirley Zhan", skill_add=12, skill_sub=85, skill_mul=42, skill_div=43)
Student.objects.create(name="Rodrigo D'Souza", skill_add=16, skill_sub=64, skill_mul=24, skill_div=97)
Student.objects.create(name="Samantha Jones", skill_add=72, skill_sub=35, skill_mul=1, skill_div=93)

students = Student.objects.all()
for student in students:
    print(student)

print('Clear Worksheets Table:')
Worksheet.objects.all().delete()

print('Make Worksheets:')
create_problems.createWorksheets()

