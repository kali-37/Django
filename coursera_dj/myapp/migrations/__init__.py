# migrations is used to store the changes made to the database
# if there was no migrations then the changes made to the database would be lost
# to migrate the changes made to the database we use the command python manage.py migrate

# and inside migrate we have __init__.py file which is a part of migrations folder
# __init__.py file is used to make the migrations folder a package

# outside the migrations folder we see __pycache__ folder
# __pycache__ folder is used to store the compiled python files
# it is used to make the code run faster
# for example if we have a file named myapp.py then the compiled file
#  will be myapp.cpython-38.pyc
