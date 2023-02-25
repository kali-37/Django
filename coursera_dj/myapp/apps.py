from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
# The main reason to have default_auto_field = 'django.db.models.BigAutoField' is to avoid the warning
# The warning is :
# django.db.models.BigAutoField is deprecated meaning that it will be removed in future versions
# The warning is because the default_auto_field is not set in the settings.py file


    name = 'myapp'
# in above class we have name = 'myapp' which is the name of the app


# for example we need to use the myapp app in the coursera_dj project
# app.py main purpose is to register the app in the project
# And the app name is myapp q