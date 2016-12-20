from django.shortcuts import render_to_response,render,redirect
from django.http import HttpResponse, JsonResponse
from django.views import View,generic
from django.views.decorators.http import require_http_methods,require_GET

from datetime import datetime

from forms import GuyForm
from models import Guy


# class home_view(generic.FormView):
#     template_name = 'guys/new_guy.html'
#     form_class = GuyForm
#     initial = {'name': 'OldDriver','email':'Kaiche@gmail.com'}
#
# class guy_detail(generic.DetailView):
#     template_name = 'guys/guy_detail.html'
#     model = Guy
#
#     def get_context_data(self, **kwargs):
#         context = super(guy_detail,self).get_context_data(**kwargs)
#         # context ['guy_detail'] = self.model.objects.get(id=self.kwargs['pk'])
#         return context
#
#     # def get_object(self):
#     #     object = super(guy_detail, self).get_object()
#     #     object.last_access = datetime.now()
#     #     object.save()
#     #     return object
#
# class guys_view(View):
#     model = Guy
#     template = 'guys/guys.html'
#
#     def post(self,request):
#         form = GuyForm(request.POST)
#         form.is_valid()
#         cd = form.cleaned_data
#         guy = self.model(name=cd['name'], age=cd['age'], email=cd['email'], phone=cd['phone'], gender=cd['gender'],last_access=datetime.now())
#         guy.save()
#         return redirect("guys")
#
#     def get(self,request):
#         guys_list = self.model.objects.all()
#         return render(request, self.template, {'guys': guys_list})

# class guys_view(generic.ListView):
#     model = Guy
#
#     def post(self,request):
#         form = GuyForm(request.POST)
#         form.is_valid()
#         cd = form.cleaned_data
#         guy = self.model(name=cd['name'], age=cd['age'], email=cd['email'], phone=cd['phone'], gender=cd['gender'])
#         guy.save()
#         return redirect("guys")


