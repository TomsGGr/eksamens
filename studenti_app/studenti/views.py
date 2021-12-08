from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentModel
from .forms import AtzimjuForma

class Student:

	def __init__(self, name, grades):
		self.name = name
		self.grades = list(map(int, grades.split(',')))

	def get_average_grade(self):
		average_grade = sum(self.grades) / len(self.grades)
		return average_grade



def skats_forma(request):

	form = AtzimjuForma(request.POST or None)

	if request.method == 'POST':

		if form.is_valid():

			student = Student(
				name=request.POST['vārds'],
				grades=request.POST['atzīmes'],
			)

			student_data_to_db = StudentModel(
				name=student.name,
				grades=student.grades,
				average_grade=student.get_average_grade(),
			)

			student_data_to_db.save()

			pievienots = 'veiksmīgi pievienots datubāzei.'

			return render(
				request,
				template_name='formas_apstiprinajums.html',
				context={'student': student_data_to_db, 'pievienots': pievienots},
			)


	return render(
		request,
		template_name='forma.html',
		context={'form': form }
	)


def skats_visi_studenti(request):

	visi_studenti = StudentModel.objects.all()

	return render(
		request,
		template_name='visi_studenti.html',
		context={'visi_studenti': visi_studenti},
	)

def skats_viens_students (request, student_id):

	student = StudentModel.objects.get(id=student_id)

	pievienots = ' '

	return render(
		request,
		template_name='formas_apstiprinajums.html',
		context={
			'student': student,
			'pievienots': pievienots,
		}
	)