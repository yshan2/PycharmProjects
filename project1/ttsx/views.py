from django.shortcuts import render,redirect
from django.http import HttpRequest


# def varifi(request):
# 	if not request.session.has_key('uid'):
# 		print('lalala')
# 		return redirect('/')
# Create your views here.

def index(request):
	context = {
		'title':'index'
	}
	return render(request,'index.html',context)



