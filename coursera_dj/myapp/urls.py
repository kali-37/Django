# this urls.py is added by user at last 

from django.urls import path , re_path




# This line is used to import the path function from the django.urls module.
# The path function is used to map the URL to the view function.
from . import views
# This line is used to import the views module from the current directory.

urlpatterns = [
    path('home/', views.index,name='index'), # if we don't write name='index' also , it works same .
    # This line is used to map the root URL to the index function in the views module.
    # The name argument is used to identify the view function.
    # This name can be used to refer to the view function in the templates.
    # The name argument is optional.
    # If you don't specify the name argument, Django will automatically generate a name for the view function.
    # The name of the view function is the name of the module followed by the name of the view function.
    # For example, if the name of the module is myapp and the name of the view function is index, the name of the view function will be myapp.index.
    # The name of the view function is used to refer to the view function in the templates.
    # For example, if the name of the view function is myapp.index, you can refer to the view function in the templates as {% url 'myapp.index' %}.
    # The name of the view function is also used to refer to the view function in the reverse function.
    # For example, if the name of the view function is myapp.index, you can refer to the view function in the reverse function as reverse('myapp.index').
    # The name of the view function is also used to refer to the view function in the {% url %} template tag.
    # For example, if the name of the view function is myapp.index, you can refer to the view function in the {% url %} template tag as {% url 'myapp.index' %}.
    # The name of the view function is also used to refer to the view function in the {% url %} template tag.
    # For example, if the name of the view function is myapp.index, you can refer to the view function in the {% url %} template tag as {% url 'myapp.index' %}.
    path('about/',views.about , name='about'),

    # Wants some drinks to drink of.
    path('drinks/<str:drink_name>', views.drinks ,name='drink_name'),

    re_path(r'^example/(?P<number>[0-9]+)/$', views.example_view),
     # Here we are using re_path to match the URL pattern.
    # The re_path function is used to map the URL to the view function.
    # The first argument is the regular expression that is used to match the URL pattern.
    # The second argument is the view function that is called when the URL pattern is matched.
    # The name argument is used to identify the view function.
    # And there inside re_path() parameter we see r'^example/(?P<number>[0-9]+)/$' , 
    # here r is used to tell python that this is a raw string. And ^ is used to match the beginning of the string.
    # And $ is used to match the end of the string.And ?P is used to capture the matched value. <number> is used to name
    #  the captured value, and it can be any name. And [0-9] is used to match any digit from 0 to 9.
    # And [0-9] is used to match any digit from 0 to 9. 
    # Also, + is isn't after ) because it is used to match one or more occurrences of
    #  the preceding regular expression. 
    # If the + symbol is placed after the group (?P<number>[0-9]) like
    #  (r'^example/(?P<number>[0-9])+/$') it will not match one or more digits but it will
    #   treat the whole group as a single character and match one or more times that group.

    #  And + is used to match one or more occurrences of the preceding regular expression.
    # Also, note the number can be greater then 9 also. And / is used to match the forward slash character.
    path('checkuserlogin/',views.checkuserlogin,name='checkuserlogin'),

    path('form_django/',views.form_view)
]