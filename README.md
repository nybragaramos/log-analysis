# Log Analysis

Project of the [Udacity Backend Nano Degree](https://eu.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## Introduction


The project build a log tool for a newspaper site that answer the 3 following questions.

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

The database contains 3 tables:

- Articles - ID, Authors ID, Title, Slug, Lead, Body and Time
- Author - ID, Authors ID and Bio 
- Log - ID, Path, IP, Method, Status, Time

## Project contents

This project consists of the following files:

- news.py - Connects to the database, executes the SQL queries and displays the results on news_log.txt.
- newsdata.zip - A zip file containing a newsdata.sql that populates the news PostgreSQL database.
- news_log.txt - A file generated by news.py containing the answers of the 3 log questions .
- Vagrantfile - Configuration file for the Vagrant virtual machine.

## System setup

1. Download [Virtual Box](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) and install.
2. Download [Vagrant](https://www.vagrantup.com/) and install.
3. Clone this repository to a directory of your choice.
4. To start up the VM run:
```bash 
$ vagrant up
```
5. To log into the VM run:
```bash 
$ vagrant ssh
```
6. To change to your vagrant directory run:
```bash 
$ cd /vagrant
```
7. Move news.py and the extracted newsdata.sql to the vagrant folder
8. To load the data and create the tables run:
```bash
$ psql -d news -f newsdata.sql 
```
9. To run the log tool run:
```bash
$ python3 news.py
```