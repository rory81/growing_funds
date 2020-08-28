[![Build Status](https://travis-ci.org/rory81/growing_funds.svg?branch=master)](https://travis-ci.org/rory81/growing_funds)
<img src=".\static\img\main_logo.jpg" alt="logo" height="25%" width="25%">

# Growing Funds 
###### Disclaimer: *this app is made for educational use only.*

## Index
1. [ Goal of GrowingFunds ](#goal)
2. [ UX and Features ](#ux)
3. [ Mock-ups ](#mock-ups)
4. [ Technologies used ](#tech)
5. [ Create a Django project ](#add_project)
6. [ Create an app within project ](#add_app)
7. [ Django admin backend ](#admin_backend)
8. [ Data Schema ](#schema)
9. [ Git Version Control ](#git)
10. [ Deployment on Heroku ](#deploy)
11. [ Cloudinary ](#cloud)
12. [ Testing ](#test)
13. [ Acknowledgements ](#thanks)

&nbsp;  
&nbsp;  
&nbsp;  
<a name="goal"></a>
## Goal of GrowingFunds
Nowadays it isn't easy to get money from a bank or get investors for a new product/project when there aren't some guarantees it will be successful.
Furthermore, peoples' dreams aren't considered much profitable. That's where crowdfunding fills the gap in the market.
Suddenly, cold hard facts aren't the only reasons to get funding anymore and likeability, sympathy and pure curiosity become very important.

This project gives people a chance to get funding for their own hobby project, their lifelong dream project or solving heartaches projects. 
<a name="ux"></a>
## UX and Features
To make sure all user stories were made or **not** made for a specific reason an Excel file was made with the following fields:
- Perspective: from which user's point of view am I looking
- Regarding: which part of the site does it apply to
- I want to be able to: what would that specific user want
- So that I can: what goal does that specific user want to achieve with that action
- Status: options were '*Not Started*', '*Ongoing*' or '*Done*' to maintain overview of the status of the entire backlog.

The User Stories where made for two kind of users:
1) The site user, looking for an interesting project to pledge to
2) A crowdfunding host, wanting to present its project to the public and get money to realise the project.

Some aspects are relevant to both group of users, like:
- able to register easily
- get an email after registration
- login and logout with email address
- possibility to reset password
- able to email the site owner in case of misuse or fraud or any other questions (note that the current email address used for the footer item is a fake and only for educational purposes. All project related email functionalities are real)
- able to update personal/delivery information in the profile page

These items are also beneficial for the admin, even though the admin isn't mentioned as a separate group. If these elements go smoothly, the less work it is for the admin to support the app.
Three user stories were not finished:
1) See how many people actually have donated. This wasn't done, because the site has the number of views to determine popularity of a project and percentage raised (and a progress bar) to see how far the host is from reaching the goal.
2) Adding Favourites. This way the user can easily find the project if they decide on a later date that they want to pledge. This issue will be added to the backlog.
3) The host can see which reward and corresponding amount is most popular by the users like a dashboard for the host. This issue will be added to the backlog.

Below the several (future) functionalities are mentioned, per user group.

##### The Site User
At first instance the user will look to the most profitable projects (top-3) or the newest projects(top-5). 
To show the popularity the user is given the number of views the projects has had. Furthermore, on the homepage the top-3 highest earners are displayed to see what is trending and maybe worthy to join in as so much is pledged already.
The simplest form to get more funding is word of mouth. So, every time the page is looked at one view is added to the total number of views of that specific project. 
To increase the word of mouth, the user has the ability to share the link of a certain project on all kinds of social media.

Secondly, the user has personal interests and wants to easily find projects that fit their personal interests.
Therefore, the projects are categorised by set categories and these categories are displayed on every page throughout the site (by putting the categories in a contexts.py).
When a user selects a certain category a table with all the projects is displayed. The table has pagination showing 5 projects by default. But 2 project per page is available, so that a mobile user can easily go through the different pages, but has an option to select 5, 10, 25 or 50 projects per page.
If the user has a (part of the) name of an interesting project it can use the search bar in the table to look for it in this particular genre.

Other ways to search for a particular project is to use the search bar present that searches through **all** projects.
Every search bar searches for words within the title as well as the description.

If a user is deciding rather of not to pledge it is important to tell them what's in it for them. In each project the project owner has to name 3 possible rewards.
The more enticing the rewards the higher the change people will pledge. For now it is necessary to fill in all three rewards so people can pledge to reward no. 1, 2 or 3.
The user can only pledge to a project when logged on and can enter an amount of their own choosing to pledge, though Stripe needs it to be higher or equal to $0.50.
For that reason, the default value is 1 and when a user accidentally enters a value lower than 1 it will return an error.

In the backlog there are a few more items to further develop this section:
1) user can select only the number of rewards that that specific project has when making a pledge.
2) when the pledged amount is lower than the amount needed for the selected reward, it should raise an error.

If the user has any questions for the host, the envelope in the project's page creates an email with the email address of the host as the recipient as well as the project title in the subject.
Once the user has pledged the user will get an email confirmation with the order number, the amount pledged and the name of the project.
Furthermore, the pledge will be shown in the projects table on the user's profile page. This way the user can see back to which projects it has pledged to and can easily return to those project pages.
On this same profile page can the user change their delivery information (address etc), although this information can also be updated when a user makes a pledge.
If the project has ended the user can no longer pledge to that project.


##### The Crowdfunding host
A project can only be started when logged on and the user has to agree to the conditions of the site to be able to publish the project. 
The content of the terms and conditions are now all made up, but are accessible by the information button next to the "Your Project" title.
Also, when the host doesn't agree to the terms and conditions the arising error will give a link to the Terms and Conditions page.

The crowdfunding host wants to be able to tell their story, in order to entice people to pledge to their project.
The CKeditor is added to enable the host to put some styling in to the story and therefore make it more attractive.
A dropdown with predefined categories is given so that there isn't a proliferation of categories, making it harder for users to find a specific project.
When there isn't an image added to the project a default image will be shown.

In the backlog there are a few more items to further develop this section:
1) crowdfunding host only obligated to fill in 1 reward, but can also make more than 3 rewards if they want to.
2) host can enter a to and from amount, so that it can be used to check if the amount for the reward is consistent with the reward chosen by the site's user.
3) the host can only add landscape pictures as the project image. Portrait images will look funny, currently the site doesn't adapt to that.
4) host can add pictures to the description and format them on the site so that layout consistency is maintained.


Any fields that have an asterisk are obligated and will raise an error:

<em>Standard Errors</em>
- Fill in these fields or this field is required, if obligated fields are empty
- Select an item in the list, if no category has been selected

Some fields needed extra help to validate and were customised:
<em>Customised Errors</em>
- Please enter a goal  higher than 0, if the goal is lower or equal to 0
- A project should be at least 30 days. If the number of days between the date of creation and the end date are lower than that an error will occur.
- Value should be higher or equal to 1 if the amount to be pledged is lower than one.

When a project is created the project will appear in the profile page. On the profile page the host can easily see how many days are left and how much it has raised as of yet.
Also the progress bar visualises the % raised. Because lower percentages (<12%) aren't visible in the progress bar a text with the percentage will be shown underneath the progress bar.
For percentages higher or equal to 12% the text will disappear and the percentage is shown in the progress bar itself.
In the same table there are buttons for the host to edit or delete the project. This way only the user that created the project can edit or delete it.
If a project is deleted, but a pledge has been made, the order history table will still show the pledge with the order number and the pledged amount.
However, the project title corresponding to this pledge will display <em>This project has been deleted</em>.
When a project is edited the goal and end date of the project are not shown and therefore not editable. 
This is to avoid a host extending the project every time it is almost ended or to manipulate the goal to their advantage.

If a user makes a pledge to the project of the host, the host will receive an email with:
- the amount, 
- the project name (just in case the host has multiple project)
- the reward chosen and
- the delivery information. The delivery information will **not** be sent if the selected option for reward is "*Nothing*".

One issue will be placed on the backlog to further improve this latter section:
1) instead of the basic email with the order details the crowdfunding host will only get an email that a new order has been placed and can see the order details in a dashboard where all placed orders can be seen and sorted through.
The host will then be able to mark them as finished if the reward has been sent.

##### admin
In case the user is an administrator the option '<em>Project Management</em>' is available to easily get access to the admin functionality from Django.
The projects, categories, email addresses, users, orders and site name can also be managed from the project management page.

##### function of the different HTML pages
The following pages were made for the users:
- project_category.html: to display all projects per selected category
- projectdetail.html: show the details for one specific project
- projects.html: homepage, showing the top-3 top earners and the last 5 projects that were newly added
- search_projects.html: page showing the results from the top search bar. Not using the homepage as there are filters (top-3 and top-5) on the projects
- startprojectform.html: form to create and publish your own project
- checkout.html: the form where the user can pledge an amount of their choosing to a project the user is interested in.
- payment_success.html: shows the results of a succeeded payment
- profile.html: shows the order history and the created projects of a user with the delivery info of the user.
- terms_and_conditions.html: the user has to agree to the terms and conditions before publishing the project. It is only fair that they can read the terms before agreeing. Note that the content is fake and for educational purposes only 
- search_projects.html: if the search bar in the header is used the results will be displayed on this page.

<a name="mock-ups"></a>
## Mock-ups
In the static folder there is also a separate folder for the mock-ups, where a PDF print out of all the mock-ups made is saved.

There are many differences between the mock-ups and the real site. This is partly due to mentor session after the first build that some layouts were changed, 
but also because some mock-ups were a bit crowded when actually build and there are multiple different pictures on it.

**Homepage:** The highest earners where displayed differently making it much less like a summation list by putting the information per project vertically instead of horizontally.
Because, this section works vertically it has a nice contrast with the new project section.
The bigger devices are displayed in the same layout as the mobile (highest earners above the new projects), because looks less crowded and calmer to the eye.

**Category:** To show the user which projects are more popular, not only the highest earner is displayed, but the most viewed was also added.
These are 2 different ways to show popularity, as a high percentage of raised money doesn't necessarily mean that the project is the most popular with the public. 
Furthermore, the highest earner and the most viewed were moved below the table with all the projects, because seeing all the other projects and searching through them is more valuable to the user.
Due to the addition of the category most viewed, the same layout (one project per category highest earner and most viewed) was maintained for the bigger devices, instead of a top 3 highest earned.

**Start Project:** Option 1 till 3 were added instead of just 1 big text area to write all rewards in.
A checkbox was added to agree to the terms and conditions of this site, as well as a picture of the coins for a consistent styling.
A new page was made to enable the user to read the Terms and Conditions (content is fake) by clicking on the information button. The latter wasn't in the mock-ups 

**Projects details:** the layout was changed after having built it. The new format was inspired by kickstart and made it possible to add more information and give it a cleaner look and less crowded.
For the mobile version the information was stacked to make it more readable. On the bigger devices the product description is now next to the reward section, so the user doesn't have to scroll up and down again when the detail information about most of the rewards are often in the description.

**Search projects:** A new page was made to display the search results when using the search bar. The search was based on the homepage and the projects displayed there all have a filter on them.
Therefore, when there were more than 5 projects fitting the search, they were not all displayed. For that reason, another page was made.

**Pledge to project:** delivery information was added, so that the host will know where to send the reward to, as well as the image of stacked coins.

**Payment successful:** additional information was added about the order and the project.

**Profile page:** This page was not in the mock-ups and was added to make the user story where a user could track their projects as well as their pledges made to other projects.


<a name="tech"></a>
## Technologies used
- [JavaScript](https://www.javascript.com/): to make Stripe elements, ShareThis button and dataTables work and to add the django-countries dropdown.
- [Django](https://www.djangoproject.com/): web framework version 3.0.8
- [Python](https://www.python.org/): Python3 is used as programming language
- [Whitenoise](http://whitenoise.evans.io/en/stable/): to serve the static files. 
- [Pillow](https://pillow.readthedocs.io/en/stable/): to be able to upload images
- [Allauth](https://django-allauth.readthedocs.io/en/latest/): addressing authentication, registration and account management
- [Stripe](https://stripe.com/en-nl): to enable the user to make payments and check credit cards
- [CKeditor](https://django-ckeditor.readthedocs.io/en/latest/): to be able to format the text entered by the user.
- [Crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/): to easily make the forms and make them user-friendly.
- [Bootstrap](https://getbootstrap.com/): to customise the html and make it responsive to different devices.
- [JQuery](https://jquery.com): to simplify DOM manipulation.
- [Gitpod](https://gitpod.io/): used as IDE
- [Heroku](www.heroku.com): used as deployment platform
- [Trello](https://trello.com/): to register the user stories and issues, so to pick up a set of issues in a certain week
- [dbdiagram.io](dbdiagram.io): to make the data schema picture
- [Cloudinary](https://cloudinary.com/): for the storage of uploaded media images, which is an alternative to AWS if you do not have an amazon account and/or a credit card.
- [html-formatter](https://www.freeformatter.com/html-formatter.html): to get the indentation correct for all html pages, using 2 spaces per indent level.



#### Template Code Institute
The template provided by Code Institute is used as basis (https://github.com/Code-Institute-Org/gitpod-full-template.git) and with this template a repository was created on GitHub by choosing the green *Use this template* button.

<a name="add_project"></a>
## How to create a django project
To use Django it needs to be installed first, so *pip3 install django==1.11.29* was used to install Django. To create a Django project where the necessary files are immediately created enter *django-admin startproject <name_project> .*
The '.' in the end is needed so the project is created in the root directory.
This will automatically create the `manage.py` file, but isn't necessarily an executable yet. So enter *chmod +x `manage.py`* in the terminal to flag this file as an executable. 

To initialize the database enter */manage.py migrate* in the terminal.
To see if the Django project is setup correctly run the project by using *python3 runserver manage.py* or *./manage.py runserver*. 
Depending on the IDE you may get an error that there is an invalid HTTP_HOST in ALLOWED_HOSTS. 
When this occurs go to the folder with your project name (in this case growing_funds) and open the *settings.py* file. Search in this file for the phrase "ALLOWED_HOSTS".
Enter the address given in the error message in the given brackets, like ALLOWED_HOSTS = ['127.0.0.1'] for instance. When the project is deployed to heroku the heroku address has to be added to this ALLOWED_HOSTS array.


<a name="add_app"></a>
### How to create an app within the main project
Within one project multiple apps can exists, each with their own urls, models, forms, etc. By adding the urls to the urls.py file in the main project, those apps become integrated in the project.

There are multiple apps in this project:
- **projects: ** contains everything regarding the content of a crowdfunding page
- **profile: ** contains everything to make a profile page with user specific information
- **checkout: ** contains everything needed to pledge to project

To add an app to the project enter python3 manage.py startapp <Name app> to the terminal. A directory with the app name will be created in the main directory.

There are few standard files/folders that come along with the creation of an app:
- **__init__.py:** An empty file that tells Python that this directory should be considered a Python package.
- **admin.py:** see next chapter *Django admin backend*
- **migrations folder:** migrations are entirely derived from your models file, and are essentially just a history that Django can roll through to update your database schema to match your current models.
- **models.py:** A model is the single, definitive source of truth about your data. It contains the essential fields and behaviours of the data you’re storing. 
- **tests.py:** for testing scripts
- **views.py:** A view function, or view for short, is a Python function that takes a Web request and returns a Web response.
- **apps.py:** to register the app in the settings.py file under **INSTALLED_APPS =** . This settings.py is created when making the Django project. This way the apps are integrated in the project.

Some files/folders are created when needed:
- **templates folder for the html files.** Besides the created apps, the main directory has also a templates folder. In the latter the base.html and the allauth html files (for authorisation) are located
- **forms.py:** here the data for the forms are defined
- **contexts.py:** to display the categories on every single page a context.py is needed. As categories are part of the projects app, the context.py file is located in this app.
- **urls.py:** per app the urls are defined. The urls are sort of linked to a view. When this url is entered in the web browser, it will call the corresponding view and will display the html output connected to that view.

<a name="admin_backend"></a>
## Django admin backend
To access the django portal in the browser, simply add */admin* after the main url (like: <your url.com>/admin).
The portal requests a username and password. This username and password can be created in the terminal by entering *./manage.py createsuperuser*

To be able to see/add/change data from the models in this backend view you need to register the model in the admin.py file.
So in this case to make the fields/data from the app Projects visible in the backend, I need to add the underlining code to the admin.py file (from the Projects folder):

*from django.contrib import admin*
*from .models import Project*

*admin.site.register(Project)*

<a name="schema"></a>
## Data schema
As the apps are integrated in the project the models from these apps can also interact with each other. So all the models combined will give the data schema for this whole project.
The picture below is the data schema for this project generated with [https://dbdiagram.io/] :

<img src=".\static\img\data_schema.png" alt="data schema" height="25%" width="100%">

The user part is from django.contrib.auth.models that is connected to UserProfile with a OneToMany relation.
UserProfile is connected to the projects and the order model, because the app needs to know who made the project and who pledges to a project.
Category is a single table, making it easier to adjust as an admin from the admin backend, used in the contexts.py
This category table is connected to the projects table in order to link a project to a certain category via a dropdown menu.

<a name="git"></a>
## Git(Hub) version control
Git is used to track the changes made and with that to have version control. The following steps are needed to track the changes made in the local repository:

**Optional: $ git status** shows all the files that have been changed, without doing anything with it

**Step 1: $ git add [file]** Snapshots the file in preparation for versioning. For [file] fill in the (path to the) filename to be versioned. Or use ```git add .``` to add all files 

**Step 2: $ git commit -m "[descriptive message]"** Records file snapshots permanently in version history. In the descriptive message a short description of the changes made are stated.

**Step 3: $ git push [file]** Uploads the local commits to GitHub. To push all files, you can just enter ```git push```
(the first time you will probably need to enter ```git push origin master```)


Branches where created to experiment with new features by using:

**Step 1: $ git branch [branch name]** To create the branch.

**Step 2: $ git checkout [branch name]** To go to that branch to work on and the previous steps to add, commit and push applies.

After the work on the branch is deemed good enough to be deployed it will be merged tot the master branch:

**Step 1: $ git checkout master** To go to the master branch.

**Step 2: $ git merge [branch name]** To merge the branch into the master branch.

Before making any commits to the repository it is important to make a *.gitignore* file in the main directory of your Django project (don't forget the dot).
Some files you do not want nor need in the git repository like:
- *.sqlite3 = database files
- __pycache__/ = compiled Python code
- latest_dump = backup file for Heroku database
- env.py = to set environment variables for development (like secret keys for instance)

<a name="deploy"></a>
## Deployment on Heroku
#### create an app
When logged on to Heroku (https://www.heroku.com/, registration needed) click the button 'New' and select the option 'Create new app'.
Give the app a name, but be aware that this should be an unique name and not previously used by you or another app on heroku.

Choose region closest by you, because then Heroku will select the edge server that is in that region, making the delivery a bit quicker.
In this case Europe was chosen.

To login to Heroku on the IDE enter 'heroku login' in the terminal and enter your credentials as requested.
However, this will not always work on Gitpod. Enter 'heroku login -i' instead and enter your credentials as requested.

By login to Heroku in the IDE a connection is created between the application in the IDE and Heroku 
that would allow to push changes (using Git) to update the application at any given time.

To check if the newly created app is connected enter 'heroku apps' in the terminal. Underneath your e-mail address a list of apps will be listed.
For this particular app 'growing-funds (eu)' is shown.

#### add needed packages and addon to make a database work
To have heroku work with a database sqlite cannot be used as it is file based, so we use postgress on Heroku which is a server-based database.
For this to work 2 packages need to be installed:
1) psycopg2: using pip3 install psycopg2-binary
2) gunicorn: using pip3 install gunicorn (to replace the development server once deployed to Heroku)

Heroku needs an addon to make postgress work. So log in to the Heroku site and go to the app.
In the app are multiple tabs, Overview, Resources, Deploy, Metrics, Activity, Access and Settings. Go to **Resources**.
Enter postgress in the search bar and select Heroku Postgress. Then select **Hobby-Dev - Free** as a plan name and click provision.

Move away from the 'Resources tab' to the tab **Settings** and click a little bit lower on *Reveal Config Vars*, the DATABASE_URL is added to the configurations.
This URL is used to connect with Django, but for that to work another package is needed: dj-database-url (pip3 install dj_database_url, be aware of the underscores).
The URL value provided by Heroku needs to be entered in the settings.py file of the project in
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get'(<DATABASE_URL'))
    }
else:
```

The else is used to set up the development part of the database and the DATABASE_URL is provided by Heroku.
Do not forget to import this addon in the top of the settings.py, right underneath the import os. (import dj_database_url)

Any changes to the models are not processed by this progress database unless migrations are made:
- python3 manage.py makemigrations --dry-run: does a trial run to see what changes there were made without doing anything else
- python3 manage.py makemigrations --dry-run: makes the actual migration
- python3 manage.py migrate --plan: is a trial run comparable to the dry-run
- python3 manage.py migrate: actually effectuate the changes to the postgress database.

These migrations are visible in the migration folder within the app directory (the app corresponding the changed model).


#### link to a Git repository
As we have already created a Git repository by using the Code Institute template, 
the next step is to add the files needed for this app to the repository by entering:
1. '$ git add .' in the terminal,
2. followed by a '$ git commit -m "message of choice"'

To associate the Heroku app as the master branch enter:
$ heroku git:remote -a <heroku app-name>
The Heroku app name will be in this case *growing-funds* 

When you push to Heroku at this point it will fail, because two additional files are needed to successfully deploy to Heroku:
1. requirements.txt : the requirements text file will contain a list of the application that are required for Heroku to run the application.
To create this file enter 'pip3 freeze --local>requirements.txt' in the terminal. A file is then generated and in the end it contains the underlining content:

- asgiref==3.2.10
- click==7.1.2
- cloudinary==1.22.0
- dj-database-url==0.5.0
- Django==3.0.8
- django-allauth==0.42.0
- django-ckeditor==5.9.0
- django-cloudinary-storage==0.2.3
- django-countries==6.1.2
- django-crispy-forms==1.9.1
- django-js-asset==1.2.2
- django-utils-six==2.0
- gunicorn==20.0.4
- itsdangerous==1.1.0
- oauthlib==3.1.0
- Pillow==7.2.0
- psycopg2-binary==2.8.5
- python3-openid==3.2.0
- pytz==2020.1
- requests-oauthlib==1.3.0
- sqlparse==0.3.1
- stripe==2.49.0
- whitenoise==5.1.0


2. Procfile (note that there isn't an extension): the Procfile is an instruction to Heroku as to which file is used as our entry point at the application.
In other words, which file is used to call the application and run it. To create a Procfile enter 'echo web: python app.py > Procfile'.
A file is created which contains the content: 

    ```web: gunicorn growing_funds.wsgi:application```

**Do not forget to add the two files to GitHub, using the previously mentioned git add and git commit.**

Now that all files are in place and everything is committed to the Git repository,  the content can be pushed to Heroku. 
Even though there aren't any static files (like CSS file or logo images), there will be an error in the logs if you deploy now.
Those static files will come sooner or later, so the collection of static files can be (temporarily) disabled with:
```$ heroku config:set DISABLE_COLLECTSTATIC=1```

Then it can be pushed to Heroku by entering ```git push heroku master``` to the terminal.
heroku logs can be checked using ```heroku logs --tail```
There will be an error displayed but that will be a Django error, indicating that the Heroku deployment succeeded.
This error indicates that this host (heroku) isn't indicated as an allowed host in Django within the settings.py like:

```ALLOWED_HOSTS = ['localhost', 'growing-funds.herokuapp.com']```
where the localhost indicates the development server.

To automatically deploy the latest code to heroku every time the git (master) branch is pushed, you will need to login to the Heroku site and go to the app.
Select the tab **Deployment**, where a button with the GitHub logo can be selected. Heroku will connect you to GitHub or ask you to login to Github.
A search bar appears where the name of the repository can be entered and click the search button. Click the connect button corresponding to the correct repository.

Underneath this section a black **Enable Automatic Deploys** can be clicked. The default setting is the git master branch, but the section underneath allows another branch to be selected.



#### configuration variables Heroku and Django
The only thing left to do is to specify some configuration variables in Heroku.
1. Login to Heroku and go to the app
2. select the Settings button from the navigation
3. Go to the section 'Config Vars' and click the Add-button
    - set the Key to 'DATABASE_URL'. Set the value of the postgress address provided by Heroku
    - set the Key to 'EMAIL_HOST_PASS'. Set the value provided by the email host, in this case Gmail.
    - set the Key to 'EMAIL_HOST_USER'. Set the value provided by the email host, in this case an email address from Gmail.
    - set the Key to 'SECRET_KEY'. Set the value to provide cryptographic signing. This key can be regenerated on https://miniwebtool.com/django-secret-key-generator/
    - set the Key to 'STRIPE_SECRET_KEY'. API key provided by Stripe Your account’s secret API key can perform any API request to Stripe without restriction.
    - set the Key to 'STRIPE_PUBLIC_KEY'. API key provided by Stripe are meant solely to identify your account with StripePublishable keys only have the power to create tokens.
    - set the Key to 'CLOUD_NAME'. Cloud name you generate when making an account.
    - set the Key to 'CLOUD_API_SECRET'. Secret key provided by Cloudinary.
    - set the Key to 'CLOUD_API_KEY'. API key provided by Cloudinary.

It is important to note that secret and API keys should not be pushed to git, but should be set as an environment variable.

Now that it is all setup click the button 'Open app' and the app is deployed.
If a "404 Not Found" appears it is probably due to a missing url in a urls.py. After ('<app_name>/') come the routes needed to make this website work for the purposes specified in the views and named in the urls.py.

When deploying the app it is important to set the DEBUG variable in the settings.py to False. This prevents showing unwanted system/code information, when an unexpected error occurs.

## Run Locally
To run locally, this repository can be cloned directly into the editor of your choice by pasting git clone  into your terminal. To cut ties with this GitHub repository, type git remote rm origin into the terminal.

The underlining steps are needed to clone this GitHub repository to another local repository:

**Step 1:** navigate to the repository for this growing_funds (login needed) *https://github.com/rory81/growing_funds*

**Step 2:** click on the green button saying **Code** with a downwards button

**Step 3:** In the Clone with HTTPs section, copy the clone URL (https://github.com/rory81/growing_funds.git) for the repository

**Step 4:** Go to the IDE that you are using (like for instance Gitpod) and open the terminal

**Step 5:** Type `git clone [URL]`. For [URL] fill in the URL that was copied in step 3 and press Enter

GitHub has another green button besides **Code**, namely the button **Gitpod**. When pushing this button the repository will be opened in the Gitpod IDE.
Step 3 to five aren't necessary anymore, unless you want a different IDE.


<a name="cloud"></a>
## Cloudinary
If you don't have a credit card you cannot make an AWS account to store the uploaded images by the user. To solve that problem, Cloudinary can be used as storage.
Heroku has an addon for this that can be connected to Heroku the same way as was done with Heroku postgress. Unfortunately, when doing this in Heroku you still need a credit card.
To avoid that an account is made on  https://cloudinary.com/ where the API keys are provided as mentioned in the deployment section of Heroku.

To setup Cloudinary, follow the setup in https://github.com/klis87/django-cloudinary-storage. 
Be aware that you do not use {{MEDIA_URL}}{{project.image}} in the template when you want to render the image, but {{project.image.url}}

<a name="test"></a>
## Testing
1. The pages are validated using:
[HTML validation](https://validator.w3.org/#validate_by_input): the django elements will create an error.
Therefor the pages where run with Chrome and **CTRL+U** was used to "view page source". This source code was entered into the validator.

The following pages where checked
- project_category.html: no errors or warnings
- projectdetail.html: the following errors occurred:
    - due to the use of the CKeditor. The CKeditor uses empty paragraph tags to indicate a line break. The HTML validator sees this as an error:
    <img src=".\static\img\bug_CKeditor.PNG" alt="bug CKeditor" height="100%" width="100%">
    
    A possible solution is to force an enter, but the CKeditor site does not recommend this and was therefore not solved.
    <img src=".\static\img\bug_CKeditor_not_recommended.PNG" alt="bug CKeditor" height="100%" width="100%">
    
    - The mailto takes as subject the {{project.title}}. This project title contains spaces. This was solved by adding %20 instead of the spaces in the title.
- projects.html : no errors or warnings
- search_projects.html : no errors or warnings 
- startprojectform.html: the following warning occurred:
    - that the type="text/javascript" attribute is unnecessary, but this JQuery is generate by the use of CKeditor.
- terms_and_conditions.html: no errors or warnings
- checkout.html: no errors or warnings
- payment_success.html: no errors or warnings
- profile.html: no errors or warnings
- the allauth templates: no errors or warnings



[CSS validation](https://jigsaw.w3.org/css-validator/#validate_by_input): no errors or warnings found

[JS validation](https://jshint.com/): the following warnings occurred
    - countryfield.js: let should be replaced by var and an unnecessary ; was removed.

[Python validation](https://extendsclass.com/python-tester.html): all views were tested and the only error was that the f'strings aren't recognised in this validator.

2. The console was checked for errors:
Only Same-site-cookie warnings where displayed. The internet was not very clear on a solution that did not have a possible negative consequence and also talked about an update the browsers needed to so in order to prevent this.
The ShareThis button gives *a Failed to load resource: net::ERR_CONNECTION_REFUSED* error, but this was due to a running VPN. When the VPN is disabled it works again.

3. Check forms:

validations were checked:
a) based on the previous list of standard and customized errors
b) a few required fields were tested for the startprojectform with Travis for educational purposes. Tests are in the tests_forms.py
c) 3 independent users made projects and made pledges.

The zoom in functionality from mobile for the forms as well as the search bars is sometimes annoying, but most of the time it is actually handy.
The users that tested it for me didn't have any trouble with it. However, the zoom function for the search bar in the datatable doesn't zoom out when the search is found.
The users didn't see this as a bug because they seem to be used to pinching in and out, but should be investigated if there is another possibility.

4. Check pagination:
all datatables were checked to see if the pagination worked, even with different number of projects.

5. check email functionality:
- checked if the user gets an email when pledging to a project
- checked if the host gets an email when a user pledges to their project
- checked allauth mail functionality

6. Tested on multiple devices:
Used the standard dev tools from Chrome to test the different devices. Also tested it live on:
- on a 1920 x 1080 screen and one size bigger screen
- tested it on an iPad (old version)
- tested it on the bigger iPad (iPad Pro 3rd generation)
- tested it on an iPhone8 and an iPhoneXR
- tested it on an android (Samsung Galaxy S20)
- put the project in the peer-code-review slack group for a week put didn't get any comments.

7. Tested the share button:
- WhatsApp
- email
- Gmail
- Yahoomail
- Facebook
- Pinterest
- if it prints out in the printer and how it comes out (projectdetail page)


<a name="thanks"></a>
## Acknowledgements
- For the basic setup of the environment of the app and its documentation the videos from Code Institute were used
and the Heroku site for a more detailed explanation of some terminology used by Heroku.

- logo picture: https://www.freepik.com/free-vector/piggy-bank-happy-piggy-bank-background_1137678.htm
- stackoverflow: every error that I got went almost through Stack Overflow
- http://gregblogs.com/the-little-things-tlt-django-creating-a-drop-down-list-with-django/
- https://www.youtube.com/watch?v=US_3XvufMLU: to set footer on the bottom of the page
- picture for when no picture is made available: Alsero-Budget-spiekozijn lqkunststoffen.nl
- https://datatables.net/manual/installation for the datatable in the category page
- https://stackoverflow.com/questions/51758405/django-give-date-field-default-value-of-one-month-from-today
- https://stripe.com/docs: to get the payments for a variable amount working
- https://www.youtube.com/watch?v=mF5jzSXb1dc&feature=youtu.be: to get the CKeditor added
- https://sharethis.com/: to get the share button to social media implemented
- the tutors from Code Institute for helping and sparring
- people on Slack when having questions
- my mentor, Maranatha Ilesanmi, for supporting and helping me when needed.
- friends and family willing to test the site for me
- https://github.com/klis87/django-cloudinary-storage: for the implementation of Cloudinary storage
