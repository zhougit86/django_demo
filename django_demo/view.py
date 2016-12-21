from django.http import HttpResponse, JsonResponse
from django.views import View,generic
import utils as rest_utils
from django.core import serializers

from guys.models import Guy

class Guys(generic.View):

    @rest_utils.ajax()
    def get(self, request):
        data = serializers.serialize('json',Guy.objects.all())
        return data