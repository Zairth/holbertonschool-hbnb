# HBnB - BL and API

## introduction

HBNB API is a web application based on Flask-RestX which provides RESTFUL architecture for users management, places, reviews and amenities.

The project follows a modular layer structure in order to separate the presentation, business logic and data persistence.

## Structure of the project
```c
hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       ├── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── facade.py
│   ├── persistence/
│       ├── __init__.py
│       ├── repository.py
├── run.py
├── config.py
├── requirements.txt
├── README.md
```

# Explanation of main folders and files

## App/
The `app/` directory contains the core application code.

## API/
The subdirectory `api/` contains endpoints of the API organized by version.

## Models/
The subdirectory `models/` defines business classes representing the main entities (e.g: User, Place).

## Services/
The subdirectory `services/` implements the facade pattern to manage the interaction between layers.

## Persistence/
The subdirectory `persistence/` is where hte in-memory repository is implemented wich he will be replaced later using SQL Alchemy.

## run.py
`run.py` is the entry point of the Flask application.

## config.py
`config.py` will manages the application configuration.

## requirements.txt
`requirments.txt` will list the dependencies necessary for the project.

# installation
## Prerequisite

***Python 3.x*** & ***Pip*** installed

## Clone the project
```c
git clone https://github.com/Zairth/holbertonschool-hbnb.git
```

## Install dependencies
```c
pip innstall -r requirments.txt
```

## Execute the application
```c
python3 run.py
```

## Authors
Luca Gimenez

Yannis Mosca Bulain

Erwan Tixerand
