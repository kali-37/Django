# this file is a part of coursera_dj project
# it is needed because it is the main file of the project
# But how a empty file be main file of the project ? 
# It is because the __init__.py file work is to make the folder as a package
# and the folder it makes package is the main file of the project which is coursera_dj
# and the settings.py file is the main file of the app which is myapp

# init makes folder package from folder 
# we need to make a folder a package because we need to import the files from that folder
# for example we need to import the settings.py file from the coursera_dj folder then 
# we need to make the coursera_dj folder a package

# example importing it as below : 

# from coursera_dj import settings

# this is the way to import the settings.py file from the coursera_dj folder