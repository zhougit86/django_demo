from django.shortcuts import render_to_response
from django.http import HttpResponse


from forms import GuyForm

def new_guy(request):
    return render_to_response('guys/new_guy.html')

def guys(request):
    values = request.GET.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def new_guy1(request):
    form=GuyForm(initial={'name': 'Xiaogang','email':'123@gmail.com'})
    return render_to_response('guys/new_guy1.html',{'form':form})

def guys1(request):
    form = GuyForm(request.GET)
    form.is_valid()
    cd = form.cleaned_data
    html=[]
    for k in cd:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, cd[k]))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))