from django.db import models
from unicodedata import name

# Create your models here.
class Menu(models.Model): #
# this is a class that inherits from models.Model , models is 
# a module that is imported from django.db and Model is a class from models module

    name=models.CharField(max_length = 100)
#.charfield is a class from models module and it takes max_length as a parameter

    cusine =models.CharField(max_length = 100)
    prices=models.IntegerField()

    def __str__(self):
# this is a special method that is used to return a string representation of an object
#here object is Menu class, so it returns a string representation of Menu class
# How a class can become a object ? 
# when we create an instance of a class, it becomes an object
# In this case instance is p=Menu() and p is an object
# we did p=Menu() in shell
# we did p=Menu.objects.get(pk=2) in shell where pk=2 , specifying 2 means
#  we are getting the object with id=2
# and we did p.save() in shell which means we are saving the object p
# so, p is an object of Menu class
# now we can use p to access the attributes of Menu class as :
# p.name
# p.cusine
# p.price
# and we can also change the values of these attributes as :
# p.name='pasta'
# Menu.objects.all() will return all the objects of Menu class 
# i.e in this case it will return all the objects of Menu class that we created in shell using
# p=Menu() and p.save()

# Now shell data is saved in database and we can access it using django admin
# whenever we save the data in shell, it is saved in database
# he can see it in path testproject/testapp/db.sqlite3/Menu

# why we actually migrate the data from shell to database ?
# because we can access the data from database using django admin
#




        return self.name + ": "+ self.cusine


'''

(Django__) ┌─[kali_37@parrot]─[~/Documents/Django__/learn_1/testproject]
└──╼ $python manage.py shell
Python 3.9.2 (default, Feb 28 2021, 17:03:44) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from testapp.models import Menu
>>> p= Menu.objects.get(pk=2) 
>>> p.cusine='chinese'
>>> p.save()
>>> Menu.objects.all()
<QuerySet [<Menu: pasta: mexican>, <Menu: Dalbhat: chinese>]>
>>> exit()

**  we did def __str__(self) so it printed " pasta:mexican and Dalbhat:chinese 
 
 So, if we comment this part in above then we would see the below when tigerred Menu.objects.all()
    # def __str__(self):
    #     return self.name + ": "+ self.cusine

>>> Menu.objects.all()
<QuerySet [<Menu: Menu object (1)>, <Menu: Menu object (2)>]>

'''