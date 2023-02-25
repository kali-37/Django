from django.shortcuts import render
 # This line is used to import the render function from the django.shortcuts module.

'''The render function is a shortcut for rendering a template with a given context. It takes the following arguments:

request: The current HTTP request object.
template_name: The name of the template to render. This can be a string containing the template name, or a Template object.
context (optional): A dictionary containing the variables to use in the template.
Here is an example of how you can use the render function to render a template called mytemplate.html with some context data:'''

# views.py can be named any as user likes .



# for forms we need to import in views.py file as well as in forms.py file
from myapp.forms import InputForm

def form_view(request):
    form=InputForm()
    context={"form":form}
    return render(request,"home.html",context)









# Create your views here.
from django.http  import HttpResponse # This line is used to import the HttpResponse class from the django.http module.

from datetime import datetime 


def index(request): # defining index function that takes {{request as a parameter}} and returns HttpResponse object.
    # Also, the index function is mapped to the root URL of the site.
    # Root url is the url that is displayed when you type the domain name of the site in the browser.
    # For example, if you type http://
    # www.google.com in the browser, the root url is http://www.google.com.
    # If you type http://www.google.com/abc in the browser, the root url is http://www.google.com/abc.
    return HttpResponse("Hello, world. You're at the polls index.") 


def sayhello(request):
    return HttpResponse("hello world ")

def homepage(request):
    return HttpResponse("Welcome to little Lemon .")

def display_date(request):
    date_joined=datetime.today().year,"/",datetime.today().month,"/",datetime.today().day 
    return HttpResponse(date_joined)

def menu(request):
    text='''<h1 style='color:#F4CE14;'> This is little lemon again!</h1>'''
    return HttpResponse(text)
    
def pathview(request,name,id):
    
    return HttpResponse(f"Name:{name} UserID:{id}")
    
def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

def showform(request):
    return render(request,"form.html")
     # it takes form.html file from templates folder inside myapp folder

def getform(request): 
    if request.method == "POST": 
        # post takes data from the form.html file as a dictionary
        # is this function auto triggered ? 
        # yes it is auto triggered when the form is submitted
        # it will get the data from the form i.e from the form.html file
        id=request.POST['id'] 
        name=request.POST['name'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 



def helo(request):
    return HttpResponse("hello world from second app _urls_2.py ")

def about(request):
    return HttpResponse("Hello kta ho it's from the another myapp> urls.py file ")

def drinks(request,drink_name):
    drink={ 
            'mocha':'type of coffee',
            'tea':'tye of hot beverage',
            'lemonade': 'type of refresment'
            }
    choice_of_drink=drink[drink_name]
    return HttpResponse(f"<h2>{drink_name}</h2>{choice_of_drink}")

def example_view(request,number):
    return HttpResponse(f"<h2> This is the provided number </h2> "+ number )

def checkuserlogin(request):
    if request.user.is_authenticated:
        return HttpResponse(f"</h4> User is logged in .</h4> username: {request.user.username}+Email: {request.user.email}+is_staff:{request.user.is_staff}")
       
    else:
        return HttpResponse(f'</h2> User is logged in </h2> username: {request.user.username}+Email: {request.user.email}+is_staff:{request.user.is_staff}')

