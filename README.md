Setting up the development server to run the project:

Install python (we’re running with python2.7.10 at the moment)

Download pip

Run the following commands:
$pip install django
$pip install widget-tweaks
$pip install Pillow

Access the main project directory which contains manage.py
Run the command:
$python manage.py runserver

Development server should now be up and running


All files have more detailed comments within
Files:

Models.py:
Contains all of the data objects used to store information (userprofiles, games, groups)

Urls.py:
Contains paths to all of the site urls

Views.py:
Handles data that is sent from the site.  There is a view for each webpage (Ex: Login view for when the user posts from the login page)

Forms.py:
This file takes care of the form fields that are sent to the template and ensures that the data entered is acceptable (Ex: When registering a username will not be accepted if it already exists)

Static folder:
Contains content such as background images

Templates folder:
Contains the html files for each view

Media folder:
Contains folder where all of the profile images are added
