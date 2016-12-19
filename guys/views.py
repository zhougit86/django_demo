from django.shortcuts import render_to_response,render,redirect
from django.http import HttpResponse
from django.views import generic


from forms import GuyForm
from models import Guy

class home_view(generic.FormView):
    template_name = 'guys/new_guy.html'
    form_class = GuyForm
    initial = {'name': 'OldDriver','email':'Kaiche@gmail.com'}


def home_page(request):
    form=GuyForm(initial={'name': 'OldDriver','email':'Kaiche@gmail.com'})
    # return render_to_response('guys/new_guy.html',{'form':form})
    return render(request,'guys/new_guy.html',{'form':form})

def view_guy(request,guy_id):
    guy = Guy.objects.get(id=guy_id)
    return render(request, 'guys/guy_detail.html', {'guy': guy})


def guys(request):
    if request.method == 'POST':
        form = GuyForm(request.POST)
        form.is_valid()
        cd = form.cleaned_data
        guy = Guy(name=cd['name'], age=cd['age'], email=cd['email'], phone=cd['phone'], gender=cd['gender'])
        guy.save()
        return redirect("guys")
    guys_list = Guy.objects.all()
    return render(request, 'guys/guys.html', {'guys': guys_list})