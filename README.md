[![Build Status](https://travis-ci.org/rory81/growing_funds.svg?branch=master)](https://travis-ci.org/rory81/growing_funds)

<img src=".\static\img\main_logo.jpg">

# Growing Funds 
###### Disclaimer: *this app is made for educational use only.*

### **Template Code Institute**
The template provided by Code Institute is used as basis (https://github.com/Code-Institute-Org/gitpod-full-template.git) and with this template a repository was created on GitHub by choosing the green *Use this template* button.


## Git(Hub) version control
Git is used to track the changes made and with that to have version control. The following steps are needed to track the changes made in the local repository:

**Step 1: $ git add [file]** Snapshots the file in preparation for versioning. For [file] fill in the (path to the) filename to be versioned.

**Step 2: $ git commit -m "[descriptive message]"** Records file snapshots permanently in version history. In the descriptive message a short description of the changes made are stated.

**Step 3: $ git push [file]** Uploads the local commits to GitHub

Branches where created to experiment with new features by using:
**Step 1: $ git branch [branch name]** To create the branch
**Step 2: $ git checkout [branch name]** To go to that branch to work on and the previous steps to add, commit and push applies.

After the work on the branch is deemed good enough to be deployed it will be merged tot the master branch:
**Step 1: $ git checkout master** To go to the master branch
**Step 2: $ git merge [branch name]** To merge the branch into the master branch


## How to create a django project
To use Django it needs to be installed first, so *pip3 install django==1.11.29* was used to install Django. To create a Django project where the necessary files are immediately created enter *django-admin startproject <name_project> .*
The '.' in the end is needed so the project is created in the root directory.
This will automatically create the manage.py file, but isn't necesarily an executable yet. So enter *chmod +x manage.py* in the terminal to flag this file as an executable.

To initialize the database enter */manage.py migrate* in the terminal.
To see if the Django project is setup correctly run the project by using *python3 runserver manage.py* or *./manage.py runserver*. Depending on the IDE you may get an error that there is an invalid HTTP_HOST in ALLOWED_HOSTS. When this occurs go to the folder with your project name (in this case growing_funds) and open the *settings.py* file. Search in this file for the phrase "ALLOWED_HOSTS".
Enter the address given in the error message in the given brackets, like ALLOWED_HOSTS = ['127.0.0.1'] for instance. When the project is deployed to heroku the heroku address has to be added to this ALLOWED_HOSTS array.


## Deployment on Heroku
When logged on to Heroku (https://www.heroku.com/, registration needed) click the button 'New' and select the option 'Create new app'.
Give the app a name, but be aware that this should be an unique name and not previously used by you or another app on heroku.

Choose region closest by you, because then Heroku will select the edge server that is in that region, making the delivery a bit quicker.
In this case Europe was choosen.

To login to Heroku on the IDE enter 'heroku login' in the terminal and enter your credentials as requested.
However, this will not work on Gitpod. Enter 'heroku login -i' instead and enter your credentials as requested.

By login to Heroku in the IDE a connection is created between the application in the IDE and Heroku 
that would allow to push changes (using Git) to update the application at any given time.

To check if the newly created app is connected enter 'heroku apps' in the terminal. Underneath your e-mail address a list of apps will be listed.
For this particular app 'the-reading-list (eu)' is shown.

As we have already created a Git repository by using the Code Institute template, 
the next step is to add the files needed for this app to the repository by entering:
1. '$ git add .' in the terminal,
2. followed by a '$ git commit -m "message of choice"'

To associate the Heroku app as the master branch enter:
$ heroku git:remote -a the-reading_list

When you push to Heroku at this point it will fail, because two additional files are needed to succesfully deploy to Heroku:
1. requirements.txt : the requirements text file will contain a list of the application that are required for Heroku to run the application.
To create this file enter 'pip3 freeze --local>requirements.txt' in the terminal. A file is then generated and contains the underlining content:

Click==7.0
dnspython==1.16.0
Flask==1.1.1
Flask-PyMongo==2.3.0
itsdangerous==1.1.0
pymongo==3.10.0
Werkzeug==0.16.0

2. Procfile (note that there isn't an extension) : the Procfile is an instruction to Heroku as to which file is used as our entry point at the application.
In other words, which file is used to call the application and run it. To create a Procfile enter 'echo web: python app.py > Procfile'.
A file is created which contains the content: 'web: python3 app.py'.

Do not forget to add the two files to GitHub, using the previously mentioned git add and git commit.

Now that all files are in place the content can be pushed to Heroku by entering 'git push heroku master' to the terminal.
To run the application with Heroku enter 'heroku ps:scale web=1' to the terminal. 

For the free version only one dyno can be used. 
Dynos are isolated, virtualized Linux containers that are designed to execute code based on a user-specified command.
In this case the web dyno is used. Web dynos are of the "web" process type that is defined in the previously generated Procfile. Only web dynos recieve HTTP traffic from routers.

When this command has run succesfully the sentence 'Scaling dynos... done, now running web at 1:Free' will appear.

The only thing left to do is to specify the IP and port by adding them as configuration variables in Heroku.
1. Login to Heroku and go to the app
2. select the Settings button from the navigation
3. Go to the section 'Config Vars' and click the Add-button
    a. set the Key to 'IP'. Set the value of IP to 0.0.0.0
    b. set the Key to 'PORT'. Set the value of PORT to 5000
    c. set the Key to 'MONGO_URI'. Set the value to mongodb+srv://rory81:<password>@myfirstcluster-nn45a.mongodb.net/<name_database>?retryWrites=true&w=majority

Now that it is all setup click the button 'Open app' and the app is deployed.
If a "404 Not Found" appears it is probably due to a missing @app.route('/'). After @app.route('/') come the routes needed to make this website work.

## Run Locally
To run locally, this repository can be cloned directly into the editor of your choice by pasting git clone  into your terminal. To cut ties with this GitHub repository, type git remote rm origin into the terminal.

The underlining steps are needed to clone this GitHub repository to another local repository:

**Step 1:** navigate to the repository for this Reading List (login needed) *https://github.com/rory81/the_reading_list*

**Step 2:** click on the green button saying **Clone or download**

**Step 3:** In the Clone with HTTPs section, copy the clone URL (https://github.com/rory81/the_reading_list.git) for the repository

**Step 4:** Go to the IDE that you are using (like for instance Gitpod) and open the terminal

**Step 5:** Type `git clone [URL]`. For [URL] fill in the URL that was copied in step 3 and press Enter

## Acknowledgements
- For the basic setup of the environment of the app and its documentation the video's from Code Institute were used
and the Heroku site for a more detailed explanation of some terminology used by Heroku.

- logo picture: https://www.freepik.com/free-vector/piggy-bank-happy-piggy-bank-background_1137678.htm