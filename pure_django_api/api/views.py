from django.views.generic import View
from django.http import HttpResponse
from updates.models import Update as UpdateModel
from .mixins import CSRFExamptMixin
import json
from updates.forms import UpdateModelForm


# Creating an End Point for Creating, Update, Retrieve and Delete Data
class UpdateModelDetailAPIView(CSRFExamptMixin, View):

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


class UpdateModelListAPIView(CSRFExamptMixin, View):

    '''
    List, Create --> Objects
    '''
    def get(self, request, *args, **kwargs):
        return HttpResponse(UpdateModel.objects.all().serialize(), content_type="application/json")

    def post(self, request, *args, **kwargs):
        form = UpdateModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return HttpResponse(obj_data, content_type="application/json", status=201)
        
        if form.errors:
            json_data = json.dumps(form.errors)
            return HttpResponse(json_data, content_type="application/json", status=400)
        
        json_data = json.dumps({'Message': 'Not Allowed'})
        return HttpResponse(json_data, content_type="application/json", status=400)

    def delete(self, request, *args, **kwargs):
        json_data = json.dumps({"message": "You cannot delete an entire list."})
        status_code = 403 # Not Allowed
        return HttpResponse(json_data, content_type="application/json", status=status_code)
    