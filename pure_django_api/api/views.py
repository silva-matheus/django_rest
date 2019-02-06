from django.views.generic import View
from django.http import HttpResponse
from updates.models import Update as UpdateModel
from .mixins import CSRFExamptMixin
import json
from updates.forms import UpdateModelForm
from .utils import is_json


# Creating an End Point for Creating, Update, Retrieve and Delete Data
class UpdateModelDetailAPIView(CSRFExamptMixin, View):

    '''
    Retrieve, update, delete --> Object
    '''

    def get_object(self, id=None):
        try:
            obj = UpdateModel.objects.get(id=id)
        except UpdateModel.DoesNotExist:
            obj = None
        return obj

    def get(self, request, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type="application/json")
    
    def post(self, request, *args, **kwargs):
        return HttpResponse({}, content_type="application/json")

    def delete(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj == None:
            error = json.dumps({"message": "Record doesn't exists"})
            return HttpResponse(error, content_type="application/json", status=404)
        delete = obj.delete()
        print(delete)
        data_response = json.dumps({"message": "Successfully delete."})
        return HttpResponse(data_response, content_type="application/json", status=201)

    def put(self, request, id, *args, **kwargs):
        print("start")
        obj = self.get_object(id=id)
        print("deu o get pelo id")
        if obj == None:
            print("Obj inválido")
            error = json.dumps({"message": "Record doesn't exists"})
            return HttpResponse(error, content_type="application/json", status=404)
        if not is_json(request.body):
            print("Json Inválido")
            error_data = json.dumps({'message': 'Invalid data sent, plese send a valid JSON.'})
            return HttpResponse(error_data, content_type="application/json", status=400)
        print("vai dar load no obj")
        passed_data = json.loads(request.body)
        saved_data = json.loads(obj.serialize())
        print("serializou o obj")
        for key, value in passed_data.items():
            saved_data[key] = value
        print("terminou de montar o obj pro update")
        form = UpdateModelForm(saved_data)
        print("deu update no modelo")
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = json.dumps(saved_data)
            return HttpResponse(obj_data, content_type="application/json", status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return HttpResponse(data, content_type="application/json", status=406)
        return HttpResponse(obj.serialize(), content_type="application/json", status=201)
    


class UpdateModelListAPIView(CSRFExamptMixin, View):

    '''
    List, Create --> Objects
    '''

    def get_object(self, id=None):
        qs = UpdateModel.objects.filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def get(self, request, *args, **kwargs):
        obj = UpdateModel.objects.all()
        if obj == None:
            error = json.dumps({"message": "Record doesn't exists"})
            return HttpResponse(error, content_type="application/json", status=404)
        return HttpResponse(obj.serialize(), content_type="application/json", status=201)

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
