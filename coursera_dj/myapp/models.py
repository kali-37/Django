from django.db import models

# Create your models here.
# Menu
# Menu Category 


class MenuCategory(models.Model):
    menu_category=models.CharField(max_length=200)

class Menu(models.Model):
    menu_item=models.CharField(max_length=200)
    price=models.IntegerField(null=False)
    category_id=models.ForeignKey(MenuCategory,on_delete=models.PROTECT ,default=None )
# Here in category_id :
# if we use on_delete =models.PROTECT 
# then it will not delete the category if it is used in menu table