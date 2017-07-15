from . import create_problems, make_history
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.staticfiles.templatetags.staticfiles import static
from .models import History, Student, Worksheet
from .forms import UploadForm
import os

STATIC_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

def get_difficulty_level(student):
	wksheet = Worksheet.objects.get(student=student)
	levels = wksheet.levels.split(',')
	categories = wksheet.categories.split(',')
	diff_lev = [0]*12
	for level, category in zip(levels, categories):
		i = int(category) * 3 + int(level)
		diff_lev[i] += 1
	return diff_lev

def index(request):
	shirley = Student.objects.get(name="Shirley Zhan")
	sam = Student.objects.get(name="Samantha Jones")
	rodrigo = Student.objects.get(name="Rodrigo D'Souza")
	add_avg = (shirley.skill_add + sam.skill_add + rodrigo.skill_add) / 3
	sub_avg = (shirley.skill_sub + sam.skill_sub + rodrigo.skill_sub) / 3
	mul_avg = (shirley.skill_mul + sam.skill_mul + rodrigo.skill_mul) / 3
	div_avg = (shirley.skill_div + sam.skill_div + rodrigo.skill_div) / 3
	averages = [add_avg, sub_avg, mul_avg, div_avg]

	context = {
		"history_shirley": History.objects.filter(student=shirley),
		"history_sam": History.objects.filter(student=sam),
		"history_rodrigo": History.objects.filter(student=rodrigo),
		"averages": averages,
		"probs_shirley": get_difficulty_level(shirley),
		"probs_sam": get_difficulty_level(sam),
		"probs_rodrigo": get_difficulty_level(rodrigo),
		"form": UploadForm()
	}
	return render(request, 'athena/index.html', context)

def upload(request):
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			files = request.FILES.getlist('file_field')
			filenames = []
			for f in files:
				filename = os.path.join(STATIC_DIRECTORY, 'athena/', fname)
				print(filename)
				filenames.append(filename)
			make_history.grade_all(filenames)
			# what to do with grades???
	return HttpResponseRedirect('/')



