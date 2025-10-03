# Airflow DAG Task

### First step 
I created new folder and add the docker compose file which is i provided in this repo
after making sure that i'm in the project's folder i ran these two commands in powerShell: 
docker compose up airflow-init


docker compose up -d

images/dcokerscreenshot.png

##
### Second step:
make sure that all containers are running and working, after that go to the airflow web server in port 8080.

you will find login page enter:
 
username: airflow

password:airflow

_you will find these info in project's yaml file_
##
### Third step:

create dagfile.py in dags folder , in this file you do the imports and write the dag and the tasks 

in my project i made 3 tasks

* print current date (BashOperator)
* Print welcome message with my name (
* Generated a random number and save it to /tmp/random.txt 

at the end of the script i ordered the tasks like this:

task1 >> task2 >> task3

#
### Forth step:
go to airflow home page and refresh, you will find a dag with the dag id you typed in the script.

## image ##
### Finally:
unpause the dag and go to the graph section you will find that all the three tasks are running successfully
### image ###

output of the task 1:image


output of the task 2:
image

output of the task 3:

image
image
