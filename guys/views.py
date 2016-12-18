from django.shortcuts import render_to_response
from django.http import HttpResponse


from forms import GuyForm
from models import Guy



def new_guy(request):
    form=GuyForm(initial={'name': 'Xiaogang','email':'123@gmail.com'})
    return render_to_response('guys/new_guy1.html',{'form':form})

def guys(request):
    if request.method == 'POST':
        form = GuyForm(request.POST)
        form.is_valid()
        cd = form.cleaned_data
        guy = Guy(name=cd['name'],age=cd['age'],email=cd['email'],phone=cd['phone'],gender=cd['gender'])
        print 'aa'

    return HttpResponse(guy.to_dict())