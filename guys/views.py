from django.shortcuts import render_to_response,render,redirect
from django.http import HttpResponse


from forms import GuyForm
from models import Guy


def home_page(request):
    form=GuyForm(initial={'name': 'OldDriver','email':'Kaiche@gmail.com'})
    # return render_to_response('guys/new_guy.html',{'form':form})
    return render(request,'guys/new_guy.html',{'form':form})

def new_guy(request):
    form = GuyForm(request.POST)
    form.is_valid()
    cd = form.cleaned_data
    guy = Guy(name=cd['name'], age=cd['age'], email=cd['email'], phone=cd['phone'], gender=cd['gender'])
    return redirect("guys")




def guys(request):

    return HttpResponse("save")