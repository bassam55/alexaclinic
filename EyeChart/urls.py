from django.conf.urls import url
from EyeChart import views

urlpatterns = [
    url(r'test/', views.index, name='index'),
    url(r'test2/', views.index2, name='index2'),
    url(r'patientform/', views.paitents, name='patients'),
    url(r'patientform2/', views.paitents2, name='patients2'),
    url(r'datatable/', views.displaytable, name='displaytable'),
]
