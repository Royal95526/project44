from django.shortcuts import render


from django.shortcuts import render
from django.db.models import Q
from django.db.models import Avg,Sum,Max,Min,Count
from website1.models import Employeee

def display_view(request):
	aa=Employeee.objects.all().aggregate(Avg('esal'))
	bb=Employeee.objects.all().aggregate(Max('esal'))
	cc=Employeee.objects.all().aggregate(Min('esal'))
	dd=Employeee.objects.all().aggregate(Sum('esal'))
	ee=Employeee.objects.all().aggregate(Count('esal'))
	my_dict={'aa':aa,'bb':bb,'cc':cc,'dd':dd,'ee':ee}
	return render(request,'website1/home.html',my_dict) 
