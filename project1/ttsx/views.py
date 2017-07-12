from django.shortcuts import render,redirect
from django.http import HttpRequest
from goods.models import goodsInfo, typeInfo

# def varifi(request):
# 	if not request.session.has_key('uid'):
# 		print('lalala')
# 		return redirect('/')
# Create your views here.

def index(request):
	goods = goodsInfo.objects
	types = typeInfo.objects
	gclass = types.all()
	context = {
		'title':'index',
		'class': gclass,


	}
	return render(request,'index.html',context)

