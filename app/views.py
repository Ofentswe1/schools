from django.shortcuts import render
from django.views import View

# Create your views here.
class Home(View):
	template_name = 'app.base.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

	def post(self, request, *args, **kwargs):
		pass


