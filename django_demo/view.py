from django.http import HttpResponse, JsonResponse
from django.views import View,generic
import utils as rest_utils

from guys.models import Guy

class Guys(generic.View):

    @rest_utils.ajax()
    def get(self, request):
        return [1,2,3]