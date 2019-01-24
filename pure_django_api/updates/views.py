from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Update
import json
from django.views.generic import View
from django.core.serializers import serialize
# Create your views here.

# def datail_view(request):
    # return render() # Return JSON data

def update_model_detail_view(request):
    # GET Request
    data = {
        "count": 10000,
        "content":  "Some New Content"
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type="application/json")
    # return JsonResponse(data)

class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        # GET Request
        data = {
            "count": 10000,
            "content":  "Some New Content"
        }
        
        return JsonResponse(data)
    
class JsonResponseMixin(object):
    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        return context

class JsonCBV2(View, JsonResponseMixin):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 10000,
            "content":  "Some New Content"
        }
        return self.render_to_json_response(data)

class SerializedView(View, JsonResponseMixin):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        data = {
            "count": obj.user.username,
            "content": obj.content
        }
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type="application/json")
        # return self.render_to_json_response(json_data)

class SerializedListView(View, JsonResponseMixin):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        data = serialize("json", qs, fields=('user', 'content'))
        # json_data = json.dumps(data)
        return HttpResponse(data, content_type="application/json")
        # return self.render_to_json_response(data)