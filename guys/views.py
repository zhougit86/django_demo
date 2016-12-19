from django.shortcuts import render_to_response,render,redirect
from django.http import HttpResponse, JsonResponse
from django.views import View,generic
from django.views.decorators.http import require_http_methods,require_GET


from forms import GuyForm
from models import Guy


class home_view(generic.FormView):
    template_name = 'guys/new_guy.html'
    form_class = GuyForm
    initial = {'name': 'OldDriver','email':'Kaiche@gmail.com'}

class guy_detail(generic.DetailView):
    template_name = 'guys/guy_detail.html'
    model = Guy

    def get_context_data(self, **kwargs):
        print kwargs
        context = super(guy_detail,self).get_context_data(**kwargs)
        # context ['guy'] = Guy.objects.get(kwargs['slug'])
        return context

class guys_view(View):
    model = Guy
    template = 'guys/guys.html'

    def post(self,request):
        form = GuyForm(request.POST)
        form.is_valid()
        cd = form.cleaned_data
        guy = self.model(name=cd['name'], age=cd['age'], email=cd['email'], phone=cd['phone'], gender=cd['gender'])
        guy.save()
        return redirect("guys")

    def get(self,request):
        guys_list = self.model.objects.all()
        return render(request, self.template, {'guys': guys_list})


def home_page(request):
    form=GuyForm(initial={'name': 'OldDriver','email':'Kaiche@gmail.com'})
    # return render_to_response('guys/new_guy.html',{'form':form})
    return render(request,'guys/new_guy.html',{'form':form})

def view_guy(request,guy_id):
    guy = Guy.objects.get(id=guy_id)
    return render(request, 'guys/guy_detail.html', {'guy': guy})

@require_http_methods(["GET", "POST"])
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

def guys_json(request):
    guys_list = Guy.objects.all()
    return JsonResponse(guys_list,safe=False)