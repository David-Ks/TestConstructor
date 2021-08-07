from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import View, ListView, CreateView, FormView, RedirectView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
import random

from .models import *
from .forms import *

# Create your views here.
class index(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'index.html')

	def post(self, request, *args, **kwargs):
		tests = [i['name'] for i in Test.objects.values('name')]
		print(request.POST['data'])
		if request.POST['data'] in tests:
			return JsonResponse('tests/' + request.POST['data'], safe=False)
		return JsonResponse('Error', safe=False)



class createTest(LoginRequiredMixin, View):
	def get(self, request):
		tests = Test.objects.all()
		return render(request, 'create.html', {'tests': tests})

	def post(self, request):
		data = request.POST['data'].split('||')
		resultMessage = request.POST['resultMessage']
		answers = 'A'
		data[1] = data[1].split('@')

		try:
			Test.objects.get(name=data[0])
			return JsonResponse('Error: Name is already taken.', safe=False)
		except:
			if (len(data[0]) >= 39):
				return JsonResponse('Error: Very long name.', safe=False)
			elif (len(data[0]) == 0):
				return JsonResponse('Error: Name is not valid.', safe=False)

			for i in data[1][0].split('#'):
				if i == '':
					return JsonResponse('Error: Empty form.', safe=False)

			for i in range(len(data[1])):
				if data[1][i]:
					data[1][i] = data[1][i].split('#')
					index = random.randint(2, 4)
					z = data[1][i][index]
					data[1][i][index] = data[1][i][2]
					data[1][i][2] = z
					answers += str(index - 1)
					data[1][i] = '#'.join(data[1][i])


			data[1] = '@'.join(data[1])
			form = Test(name = data[0], author = request.user, questionsAndAnswers = data[1], result = resultMessage, answers=answers)
			form.save()
			return JsonResponse('Ok', safe=False)


class testList(ListView):
	model = Test
	template_name = 'testlist.html'
	context_object_name = 'tests'


class testPage(View):
	def get(self, request, *args, **kwargs):
		try:
			test = Test.objects.get(name=kwargs['test_name'])
			return render(request, 'testpage.html', {'test': test})
		except:
			return render(request, 'error.html')


class Registration(CreateView):
	template_name = 'registration.html'
	form_class = UserRegisterForm
	success_url = reverse_lazy('index')
	object_list = []

	def form_valid(self, form):
		form = super(Registration, self).form_valid(form)
		username = self.request.POST['username']
		password = self.request.POST['password1']
		userauth = authenticate(self.request, username=username, password=password)
		if userauth is not None:
			login(self.request, userauth)
		return form


class User_logout(RedirectView):
	url = reverse_lazy('login')
	def get(self, *args, **kwargs):
		logout(self.request)
		return super(User_logout, self).get(self, *args, **kwargs)


class User_login(FormView):
	form_class = UserLoginForm
	template_name = 'login.html'
	success_url = reverse_lazy('index')

	def form_valid(self, form):
		username = self.request.POST['username']
		password = self.request.POST['password']
		userauth = authenticate(self.request, username=username, password=password)
		if userauth is not None:
			if userauth.is_active:
				login(self.request, userauth)
		return super(User_login, self).form_valid(form)


class AboutUs(TemplateView):
	template_name = 'aboutus.html'



