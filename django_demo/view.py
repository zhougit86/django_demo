from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.views import View,generic
import utils as rest_utils
from django.core import serializers
import json

from guys.models import Guy

class Guys(generic.View):

    @rest_utils.ajax()
    def get(self, request):
        data = serializers.serialize('python',Guy.objects.all())
        return data

    @rest_utils.ajax()
    def post(self, request):
        raw = request._body
        raw = json.loads(raw)
        guy = Guy(name=raw['name'], age=raw['age'], email=raw['email'], phone=raw['phone'], gender=raw['gender'],last_access=datetime.now())
        guy.save()
        return {"status": "success", "msg": "success"}
