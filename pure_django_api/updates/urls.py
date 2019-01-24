from django.urls import path
from . import views

urlpatterns = [
    path('', views.update_model_detail_view, name='update'),
    path('jsonCBV', views.JsonCBV.as_view(), name='jsonCBV'),
    path('jsonCBV2', views.JsonCBV2.as_view(), name='jsonCBV2'),
    path('serializedView', views.SerializedView.as_view(), name='serializedView'),
    path('serializedListView', views.SerializedListView.as_view(), name='serializedListView'),
]