from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response

import datetime

def hello(request,name):
    now = datetime.datetime.now()
    t = Template("<html><body>Hello {{name.capitalize}}, It's {{ current_date }}.</body></html>")
    html = t.render(
        Context({'current_date': now,'name': name})
    )
    return HttpResponse(html)

def hello_template(request,name):
    now = datetime.datetime.now()
    t = get_template("greeting.html")
    html = t.render(
        Context({'current_date': now,'name': name})
    )
    return HttpResponse(html)

def hello_shortcut(request,name):
    now = datetime.datetime.now()
    c = Context({'current_date': now,'name': name})
    return render_to_response("extends.html",c)