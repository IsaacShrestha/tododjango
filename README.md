# Karyalaya django / tododjango

This django api is built as a backend for ember application Karyalaya present in the repository https://github.com/IsaacShrestha/todoember.git. 
Kindly clone this repository and follow the installation guide mentioned there to view the complete functions of the application.


#Prerequisites to run this application
1) python 2.7    &   
2) django 1.9.8

#Installation guide
To install this app you will need to install several django dependencies first. You may want to do this in an isolated environment other 
than on your test server. Please follow the steps mentioned below

* Clone this repository by typing,   git clone https://github.com/IsaacShrestha/tododjango.git  
* cd to the django directory,   cd tododjango
* install django:   pip install django==1.9.8
* install rest framework:   pip install djangorestframework
* install rest framework filters:   pip install djangorestframework-filters
* install cors-headers:   pip install django-cors-headers
* install jsonapi:   pip install djangorestframework-jsonapi
* install markdown:   pip install markdown


#Running the app

* cd to the django directory, e.g. ../tododjango/
* Launch runserver, python manage.py runserver
* View the app in your browser at localhost:8000


#User guide

This application allows you to do the followings:
* Register your account
* Login using the username and password
* Add the jobs 

When you come to the website for the first time, to begin using the service you need to register as either a job seeker or a job poster. Once, you are registered you can login using username and password.

In this version only job poster's panel is fully functional. As soon as you login as job poster, your dashboard will be empty. By choosing add new job you can add the job. You can select add, edit and delete the jobs from your dashboard as a job poster.
