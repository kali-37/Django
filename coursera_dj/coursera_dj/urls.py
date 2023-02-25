# This urls.py file is from /home/kali_37/Documents/django/coursera_dj/coursera_dj/urls.py
# It is different from another urls.py from /home/kali_37/Documents/django/coursera_dj/myapp/urls.py
#this is urls.py file in coursera_dj folder.But we have urls.py file in myapp folder also.
#The difference between these two urls.py files is that :
# The urls.py file in the coursera_dj folder is the project-level urls.py file ,where as 
# the urls.py file in the myapp folder is the application-level urls.py file.
#And urls.py file in the coursera_dj folder or project folder is the main urls.py file,where as 
# urls.py file in the myapp folder or application folder is the sub urls.py file.
#urls.py in coursera_dj folder is used to map the root url to the index function in the views.py file in the myapp folder.

"""coursera_dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp import views


urlpatterns = [ # this bracket is used to define a list of url patterns.
# here can exists many url patterns in this list.

    path('admin/', admin.site.urls),
    path('little/', include('myapp.urls')),# first it takes little/home ' where /home is from myapp.urls ko '
    # And this is the same when we do from django.urls import reverse and reverse('index')
    # gives us '/little/home' .But we can have application name in app wala urls.py and set
    # it's path as '' just .
    # for instance :
    # in app wala urls.py we wiil have 
    # app_name = 'myapp' # this is the name of the application
    # path('', views.index,name='index'), # if we don't write name='index' also , it works same .


    # from second urls_2.py 
    path('second/', include('myapp.urls_2')),
    path('say_hello/',views.sayhello),
    path('homepage/',views.homepage),
    path('date_time/',views.display_date),
    path('menu',views.menu),
    path('getuser/<name>/<id>',views.pathview,name='pathview'),
    path('getuser/', views.qryview, name='qryview'),
    path('getform/', views.getform),
    path('showform/', views.showform, name='showform')


]
# this is another path added for views.py in coursera_dj which views.py was created by me.
handler404 ='coursera_dj.views.handler404'
 # this is the path to the handler404 function in views.py in coursera_dj folder.
 # it is written outside of the list of url patterns because it is not a url pattern.
# it is a path to the handler404 function in views.py in coursera_dj folder.

