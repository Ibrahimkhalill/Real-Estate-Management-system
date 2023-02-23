from django.urls import path
from . import views
urlpatterns = [
    path('add_broker',views.add_broker,name='add_broker'),
    path('add_properties',views.add_properties,name='add_properties'),
    path('view_properties',views.view_properties,name='view_properties'),
    path('edit_properties/<int:pk>',views.edit_properties,name='edit_properties'),
    path('delete_properties/<int:pk>',views.delete_properties,name='delete_properties')


]
