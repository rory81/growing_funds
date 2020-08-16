
<img src=".\static\img\main_logo.jpg" alt="logo" height="25%" width="25%">

# Growing Funds 
###### Disclaimer: *this app is made for educational use only.*
Nowadays it isn't easy to get money from a bank or get investors for a new product/project when there aren't some garantees it will be successfull.
Furthermore, peoples dreams aren't considered much profitable. That's where crowdfunding fills the gap in the market.
Suddenly, cold hard facts aren't the only reasons to get funding anymore and likebility, sympathy and pure curiosity become very important.

This project gives people a change to get funding for their own hobby project, their life long dream project or solving heartaches projects. 

## UX and Features
The User Stories where made for two kind of users:
1) The site user, looking for an interesting project to pledge to
2) A crowdfunding host, wanting to present its project to the public and get money to realise the project.

Some aspects are relevant to both users, like:
- able to register easily
- get an email after registration
- login and logout with emailaddress
- possibility to reset password
- able to email the site owner in case of misuse or fraud or any other questions
- able to update personal/delivery information in the profile page


##### The Site User
At first instance the user will look to the most popular projects or the newest projects. 
To see the newest project, the top-5 newest projects are displayed on the homepage.

To show the popularity the user is given the number of views the projects has had. Furthermore, on the homepage the top-3 highest earners are displayed to see what is trending.
The simplest form to get more funding is word of mouth. So, everytime the page is looked at one view is added to the total number of views of that specific project. 
To increase the word of mouth the user has the ability to share the link of a certain project on all kinds of social media.

Secondly, the user has personal interests and wants to easily find projects that fit their personal interests.
Therefore, the projects are categorised by set categories and these categories are displayed on every page throughout the site.
When a user selects a certain category a table with all the projects is displayed. The table has pagination showing 2 projects by default, but has an option to select 5, 10, 25 or 50 projects per page.
If the user has a (part of the) name of an interesting project it can use the searchbar in the table to look for it in this particular genre.

Other ways to search for a particular project is to use the search bar present that searches through **all** projects.
Every searchbar searches for words within the title as well as the description.

If a user is deciding rather of not to pledge it is important to tell them what's in it for them. In each project the project owner has to name 3 possible rewards.
The more enticing the rewards the higher the change people will pledge. For now it is necessary to fill in all three project so people can pledge to reward no. 1, 2 or 3.
The user can only pledge to a project when logged on.

In the backlog there are a few more items to further develop this section:
1) crowdfunding host only obligated to fill in 1 reward, but can also make more than 3 rewards if they want to.
2) user can select only the number of rewards that that specific project has when making a pledge.
3) when the pledged amount is lower than the amount needed for the selected reward, it should raise an error.

If the user has any questions for the host, the envelope in the project's page creates an email with the email address of the host as the recipient.
Once the user has pledged the user will get an email confirmation with the order number, the amount pledged and the name of the project.
Furthermore, the pledge will be shown in the projects table  on the user's profile page. This way the user can see back to which projects it has pledged to. 
On this same profile page can the user change their delivery information (address etc), although this information can also be updated when a user makes a pledge.


##### The Crowdfunding host
A project can only be started when logged on and the user has to agree to the conditions of the site to be able to publish the project.

The crowdfunding host wants to be able to tell their story, in order to entice people to pledge to their project.
The CKeditor is added to enable the host to put some styling in to the story and therefore make it more attractive.
A dropdown with predefined categories are given so that their isn't a proliferation of categories, making it harder for users to find a specific project.
When there isn't an image added to the project a default image will be shown.

Any fields that have an asterisk are obligated and will raise an error:

<em>Standard Errors</em>
- Fill in these fields, if obligated fields are empty
- Select an item in the list, if no category has been selected


<em>Customised Errors</em>
- Please enter a goal amount higher than 0, if the amount is lower or equal to 0
- A project should be at least 30 days. If the number of days between the date of creation and the end date are lower than that an error will occur.
- As mentioned before, the host has to agree to the terms and conditions. If there is no agreement an error will occur.

When a project is created the project will appear in the profile page. On the profile page the host can easily see how many days are left and how much it has raised.
In the same table there are buttons for the host to edit or delete the project. This way only the user that created the project can edit or delete it.
If a project is deleted, but a pledge has been made, the table will still show the pledge.
However, the project title corresponding to this pledge will display <em>This project has been deleted</em>.
When a project is edited the goal and end date of the project are not shown and therefore not editable. This is to avoid a host extending the project every time it is almost ended.




## Template Code Institute
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
This will automatically create the `manage.py` file, but isn't necesarily an executable yet. So enter *chmod +x `manage.py`* in the terminal to flag this file as an executable. 

To initialize the database enter */manage.py migrate* in the terminal.
To see if the Django project is setup correctly run the project by using *python3 runserver manage.py* or *./manage.py runserver*. Depending on the IDE you may get an error that there is an invalid HTTP_HOST in ALLOWED_HOSTS. When this occurs go to the folder with your project name (in this case growing_funds) and open the *settings.py* file. Search in this file for the phrase "ALLOWED_HOSTS".
Enter the address given in the error message in the given brackets, like ALLOWED_HOSTS = ['127.0.0.1'] for instance. When the project is deployed to heroku the heroku address has to be added to this ALLOWED_HOSTS array.

### How to create an app within the main project
Within one project multiple apps can exists, each with their own urls, models, forms, etc. By adding the urls to the urls.py file in the main project, those apps become integrated in the project.

There are multiple apps in this project:
- **projects: ** contains everything regarding the content of a crowdfunding page
- **auth: ** contains everything regarding the authorisation to the page
- **payment: ** contains everything needed to back a project financially

To add an app to the project enter *./manage.py startapp <Name app>* to the terminal. A directory with the app name will be created in the main directory.

## Django admin backend
To access the django portal in the browser, simply add */admin* after the main url (like: <your url.com>/admin).
The portal requests a username and password. This username and password can be created in the terminal by entering *./manage.py createsuperuser*

To be able to see/add/change data from the models in this backend view you need to register the model in the admin.py file.
So in this case to make the fields/data from the app Projects visible in the backend, I need to add the underlining code to the admin.py file (from the Projects folder):

*from django.contrib import admin*
*from .models import Project*

*admin.site.register(Project)*



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
- stackoverflow (https://stackoverflow.com/questions/31130706/dropdown-in-django-model)
- http://gregblogs.com/the-little-things-tlt-django-creating-a-drop-down-list-with-django/
- https://codepen.io/mahish/pen/RajmQw
- https://www.youtube.com/watch?v=US_3XvufMLU: to set footer on the bottom of the page
- picture for when no picture is made available: Alsero-Budget-spiekozijn lqkunststoffen.nl
- https://datatables.net/manual/installation for the datatable in the category page
- https://stackoverflow.com/questions/51758405/django-give-date-field-default-value-of-one-month-from-today
- https://www.youtube.com/watch?v=oZwyA9lUwRk&t=1454s : Stripe for a donation page 