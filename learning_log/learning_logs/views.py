from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
	topic = Topic.objects.all()
	return render(request,'index.html',{'topic':topic})