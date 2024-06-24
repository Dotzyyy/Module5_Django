# Module5_Django
## django projects app w/ postgres sql
Flask Blog 2
Render Url: https://module5-django.onrender.com
Github Url: https://github.com/Dotzyyy/Module5_Django
Super User: username: superadmin
            password: superpassword1234

## Concept

This app is a blog style website aimed at displaying project information where users can sign up and inspect the projects of other users. They can also privately message each other using an inbox feature.

### Languages and Technology Used

Featured Languages:

* HTML5

* CSS3

* JavaScript

* Python3

* SQL

Featured Technologies:

* Postgresql

* pgadmin

* Bootstrap 

* Flask

* AWS S3 (for image hosting)

* Render (For deploying the app)

### Features



* Forms are available to help register, login, edit information and make blog posts on the site.

* Forms for creating , updating and deleting posts.

* Requesting a new password be sent to your email

* Forms for sending andreceiving private messages.

* Areas to view received and sent messages, with the option to archive or delete said items.

* Feeback on successful deletions and archiving of messages.

* Live updates in the message inbox for new messages and visual prompts for which are the unread messages.








### Current Problems and Future Updates.

Maybe not so much an update but I had a problem displaying images when I deployed the website the render or deployed it locally with DEBUG off. 
When I checked the devconsole and debug files it returned a 404 error. I tried everything from the reconfiguring the media and static files to changing the urls in the templates. I eventually went and decided to creat an AWS account and use the S3 service to host the images externally. While it solves the problem now, it would not do for a larger website as the AWS is a paid service. The problem occured to me to late in development to ask during the Saturday coding sessions.

Email reset function has been tempremental, it works locally with debug mode on and off but not always when I deploy to render. Gmail is flagging my site as untrusworthy so I have put in a request with google to unblock it. Have yet to hear back

## How to run the database on render

### Step 1:

Sign in or create an account on https://render.com/

### Step 2:

On the Dashboard, create new PostgreSQL database and fill in the various details.

### Step 3:

Once created, download a database management software such as Postgresql and PgAdmin.

### Step 4: 

Create a new server node, click properties and navigate to the connection tab.
Enter the following from the render database'S EXTERNAL URL:

* Host name/address. 

* Port should be automatic but look something like: 5432

* Maintenance database

* Username. For example: davidsexton

If entered correctly, the render database should appear in your servers.

### Step 5:

In your settings.py write something like 
"DATABASES = {
    'default': dj_database_url.parse(database_url)}
database_url = os.environ.get("DATABASE_URL")".

Later on in your render environment, make sure DATABASE_URL = the render databases INTERNAL_URL

### Step 6:

Use your terminal to type python manage.py migrate and then python manage.py makemigrations in order to create the database tables.

### Step 7:
At this point you'll need to have created to webservice so return to this step once that is complete.

Place an environment variable in the web service's environment tab called 'DATABASE_URL' and paste the Internal URL from the render database. Also create another variable named
Do not forget that the address should begin with 'postgresql'! / The rest of the environment variables will be provided on the UCD LMS

*Example: 'postgresql://davidsexton:hFNESpygwyQd4DMpWiBliSWZRbmwibRY@dpg-cpisitkf7o1s73bm97o0-a/flask_project_db_e6in' NOT ''postgres://davidsexton:hFNESpygwyQd4DMpWiBliSWZRbmwibRY@dpg-cpisitkf7o1s73bm97o0-a/flask_project_db_e6in'
            


## How to Deploy/Access the main website

### Step 1:

One of three options:

* Upload the project folder to your own github.

* Clone this git repository at: https://github.com/Dotzyyy/Module5_Django

* Access via the provided URL: https://module5-django.onrender.com

### Step 2:
    
   Sign in or create an account on https://render.com/

### Step 3:

    Link your github account

### Step 4:

   Once logged in and on the main dashboard, select "New" > "Web Service".

### Step 5:

    Connect to this repository or a clone of it.

### Step 6:

On the following form, ensure that:

* You select an appropriate name for the web service

* Select your closest region (Frankfurt for Europe)

* Branch should be 'main'

* Run the following commands: pip install -r requirements.txt ; python manage.py migrate ; python manage.py collectstatic ; python manage.py ensure_adminuser
    Do not forget the ';' after each command

* Start Command 'gunicorn django_project.wsgi:application'

* Select Instance Type 'free

* Use the .env file provided in the zipfile on the UCD LMS

### Step 7:

Use the provided Url to access the website!:
    https://module5-django.onrender.com

### Step 8:

You can use your own gmail to test out password reset just make sure 2fa is enabled and you generate an app password for render.
Place them under EMAIL_USER and EMAIL_PASS respectively.