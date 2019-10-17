# Fenix-challenge
This repository contains the two interview questions assigned to me by Fenix International.
Each question implementation resides on a separate branch.

## Question One
This program enables customers to calculate the number of days of lighting they have based on how much they pay for the loans they have.

To access question one please check out to the `Question-1` branch

Run `git checkout Question-1`

### How run the question one program
First you will have to install the project dependencies

Run `pip install -r requirements.txt`

Make sure you have your virtual environment activated

To setup the virtual environment

Run `python -m venv venv` and then `.venv/bin/activate` to activate the virtual environment

After this you can now run the project.

In your terminal navigate to the main directory

Run `cd main`

In the `main.py` file call the `compute_days_of_lighting` function and provide the required arguments

Now head back to the terminal and run `python main.py`

This will run the `compute_days_of_lighting` function which will compute the number of days of lighting the customer has.

To run the tests Run `pytest tests/test.py`


## Question two
This is a commandline app that enables users to make payments for products using mtn mobile money.

The project is integrated with the mtnmomo api

To access question two please check out to the `Question-2` branch

Run `git checkout Question-2`

### How run the question two program
First you will have to install the project dependencies

Run `pip install -r requirements.txt`

Make sure you have your virtual environment activated

To setup the virtual environment

Run `python -m venv venv` and then `.venv/bin/activate` to activate the virtual environment

### Install and Setup redis

#### Make migrations
Run `python manage.py makemigrations` This should setup the migration files

Run `python manage.py migrate` This will make the actual migrations

After this you can now run the project.

Run `python manage.py pay` and follow the prompt to make a payment


### Author
Name : sanya kenneth

Email: sanyakenneth@gmail.com
