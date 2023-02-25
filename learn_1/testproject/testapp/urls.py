from django.urls import path

from . import views

urlpatterns=[

    path('',views.index,name='index'),
    path('<int:id>/<str:name>/',views.getr,name='getr'),
    path('<int:id>',views.checkid,name="idcheck")


]