from django.views.generic import View
from django.http import HttpResponse
from updates.models import Update as UpdateModel


# Creating an End Point for Creating, Update, Retrieve and Delete Data
class UpdateModelDetailAPIView(View):

    '''
    Retrieve, update, delete --> Object
    '''
    def get(self, request, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type="application/json")
    
    def post(self, request, *args, **kwargs):
        return HttpResponse({}, content_type="application/json")

    def put(self, request, *args, **kwargs):
        return HttpResponse({}, content_type="application/json")

    def delete(self, request, *args, **kwargs):
        return HttpResponse({}, content_type="application/json")


class UpdateModelListAPIView(View):

    '''
    List, Create --> Objects
    '''
    def get(self, request, *args, **kwargs):
        return HttpResponse(UpdateModel.objects.all().serialize(), content_type="application/json")

    def post(self, request, *args, **kwargs):
        return HttpResponse({}, content_type="application/json")
    