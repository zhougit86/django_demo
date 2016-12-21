from django.http import HttpResponse, JsonResponse
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
        guy = request._body
        print guy.name