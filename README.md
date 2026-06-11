# Task-Manager-using-Flask

A simple web application to store your To-Do Tasks .

# Features

- User Authentication
- Easy to use and deploy locally.


# Setup for run locally

## Clone
Clone the repository and open it using the following commands:

   ```git clone git@github.com:wcipriano/case-study-hdb-task-manager.git```

   ```cd  case-study-hdb-task-manager```

## Setup python

Install python version >= 3.11 like this example: 

   ```sudo apt install python3.11 python3.11-venv ```

Install virtual env like this example:

   ```python3.11 -m venv .venv```

Activate virtual env

   ```source ./.venv/bin/activate```


## Setup app

1. Requirements

Execute the following command to install the required third party libraries, and then, open app dir:

   ```pip3 install -r requirements.txt```

   ``` cd todo_project ```


2. Create .env file

    ```echo -e "FLASK_APP=todo_project\nFLASK_ENV=development\nFLASK_DEBUG=1\nFLASK_RUN_PORT=8080" > .env```


4. Run this command to start the application

    ``` flask run ```


# Usage

1. Setup database 
    
    ```bash
    flask db init 
    flask db migrate -m "Init DB"
    flask db upgrade
   ```

2. Open url in your favorite browser and enjoy:
   http://localhost:8080


# Results

## Registration Page
Login or Register if you dont have an account

![Registration Page](output/register.jpg)

## Accessing URL's 
User cannot access any URL's if they are not logged in

![Invalid Access](output/invalid-access.jpg)

## After Successfull Login
See all your tasks after successfull login.

![After Login](output/after-login.jpg)

## Add Tasks
Click the **Add Task** link in the side-bar to add tasks

![Image of Yaktocat](output/add-task.jpg)

## View All Tasks
Click the **View All Task** link in the side-bar to see all tasks. You can **Update** and **Delete** Tasks from this page.

![Image of Yaktocat](output/all-tasks.jpg)

## Account Settings
Change your username and password. You can access this by clicking dropdown in the Navbar

![Image of Yaktocat](output/account-settings.jpg)

