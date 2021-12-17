# Exoplanet Web-App


## How App Fulfils the Brief

This is a microservice application built using Flask.

The application is built in the Python base microservice framework Flask.

Data is stored in a MySQL database.

The app keeps track of one entity, exoplanets. The app has CRUD functionality. The navigation bar allows a user to access the "Enter Data" page where new data can be added. It also allows access to the "Delete" page where data can be deleted by entering the id of a record.

The index page reads the data currently in the database and displays it on the screen.

Update is functionality is accessed by visiting the page `http://[ip-address]/update/id`. Updating a particular record is possible by supplying the id.

## How the application works

## How the pipeline works

## Unit Tests Report

## Improvements

|     |        | Exoplanet |                     |
| --- | ------ | --------- | ------------------- |
|     | **pk** | **id**    | **int**             |
|     |        | name      | varchar(32), Unqiue |
|     |        | system    | varchar(32)         |
|     |        | method    | varchar(32)         |
|     |        | year      | int                 |
